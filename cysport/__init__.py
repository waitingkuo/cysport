from flask import Flask

def create_app(config_filename):

    # Init App 
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile(config_filename)


    # Register Assets
    from cysport.assets import register_assets
    register_assets(app)


    # Init DBs

    # Init Views
    with app.app_context():
        from cysport import views


    return app

