from flask import Flask, render_template
from app.extensions import db, migrate, login_manager


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extensions(app)
    # register_blueprints(app)

    @app.route('/')
    def home():
        return render_template("home.html")
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


