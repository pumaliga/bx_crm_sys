from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from .views import views
    app.register_blueprint(views)

    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    return app
