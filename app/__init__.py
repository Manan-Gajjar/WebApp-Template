from importlib import import_module

from flask import Flask, url_for, redirect, request
from werkzeug.exceptions import InternalServerError

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_caching import Cache

from config import config
import os
import decimal
import flask.json

import logging


logger = logging.getLogger(__name__)

db = SQLAlchemy()
csrf = CSRFProtect()
cache = Cache()

class MyJSONEncoder(flask.json.JSONEncoder):
    """Custome json encoder for flask to handle Decimal object"""
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(MyJSONEncoder, self).default(obj)


def create_app(config_name):
    
    app = Flask(__name__, static_folder='base/static')
    
    app.config.from_object(config[config_name])

    app.json_encoder = MyJSONEncoder

    db.init_app(app)
    csrf.init_app(app)
    cache.init_app(app)

    # Register blueprint(s)
    for module_name in ['base', 'dummy_dashboards']:

        module = import_module(f'app.{module_name}.routes')
        app.register_blueprint(module.blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for('base_blueprint.page_not_found'))
    
    @app.errorhandler(InternalServerError)
    def handle_500(e):
        return redirect(url_for('base_blueprint.internal_server_error'))
    
    return app