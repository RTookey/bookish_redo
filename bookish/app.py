from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ['APP_SETTINGS'])

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    Migrate(app, db)

    CORS(app)

    from bookish.controllers.BookController import book_controller
    app.register_blueprint(book_controller)

    from bookish.controllers.UserController import user_controller
    app.register_blueprint(user_controller)

    from bookish.controllers.AuthController import auth_controller
    app.register_blueprint(auth_controller)

    return app

