from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from . import models
    from app.models import Users

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    from .views import views
    app.register_blueprint(views)

    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/auth')

    from .profile import profile as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/profile')

    return app
