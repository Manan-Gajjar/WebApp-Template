import os
import urllib

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DATABASE_CONNECT_OPTIONS = {}

    # Turn off Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY')

    # Application insight
    INSTRUMENTATION_KEY = os.environ.get('INSTRUMENTATION_KEY')

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET'

    # Flask-Caching related configs
    CACHE_TYPE = "SimpleCache"  
    CACHE_DEFAULT_TIMEOUT = 1500

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    dev_params = urllib.parse.quote_plus(os.environ.get('SQLCONNSTR_DEVSQL_SERVER'))
    prod_params = urllib.parse.quote_plus(os.environ.get('SQLCONNSTR_PRODSQL_SERVER'))

    SQLALCHEMY_BINDS = {
    'AZSDB_MOSAIC_DEV' : f"mssql+pyodbc:///?odbc_connect={dev_params}",
    'AZSDB_MOSAIC_PROD': f"mssql+pyodbc:///?odbc_connect={prod_params}",
    }

    DEBUG = False

class DevelopmentConfig(Config):
    dev_params = urllib.parse.quote_plus(os.environ.get('SQLCONNSTR_DEVSQL_SERVER'))
    prod_params = urllib.parse.quote_plus(os.environ.get('SQLCONNSTR_PRODSQL_SERVER'))

    SQLALCHEMY_BINDS = {
    'AZSDB_MOSAIC_DEV' : f"mssql+pyodbc:///?odbc_connect={dev_params}",
    'AZSDB_MOSAIC_PROD': f"mssql+pyodbc:///?odbc_connect={prod_params}",
    }

    DEBUG = True

class LocalConfig(Config):
    params_local = urllib.parse.quote_plus(os.environ.get('LOCAL_DB'))
    
    SQLALCHEMY_BINDS = {
    'AZSDB_MOSAIC_DEV' : f"mssql+pyodbc:///?odbc_connect={params_local}",
    'AZSDB_MOSAIC_PROD': f"mssql+pyodbc:///?odbc_connect={params_local}",
    'LOCAL_DB'         : 'sqlite:///local.db'
    }

    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'local':LocalConfig
}