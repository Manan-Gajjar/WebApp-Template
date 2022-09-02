from flask import render_template
from app.base import blueprint


# Application error handling
@blueprint.route('/')
def landing_page():
   return render_template("landing_page.html")

# Application error handling
@blueprint.route('/403')
def access_denied():
   return render_template("error_template/403.html")


@blueprint.route('/404')
def page_not_found():
    return render_template("error_template/404.html")


@blueprint.route('/500')
def internal_server_error():
    return render_template("error_template/500.html")