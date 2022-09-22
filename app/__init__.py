from flask import Flask, render_template

import app
from app.extensions import db, migrate, login_manager
from app.models import User


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extensions(app)
    register_blueprints(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return render_template("home.html")
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


def register_blueprints(app):
    from app.user.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')



