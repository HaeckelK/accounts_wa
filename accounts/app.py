from flask import Flask

UPLOAD_FOLDER = '../uploads'


def create_app():
    app = Flask(__name__.split(".")[0])

    from accounts.imports import bp as imports_bp
    app.register_blueprint(imports_bp)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # TODO move to config.ini
    app.config['DBFILENAME'] = '../accounts.db'
    # TODO move out of version control
    app.secret_key = 'fdnifadfodkm'
    return app
