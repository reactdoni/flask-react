from flask_restx import Api
from flask import Flask
from models import Recipe, User
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from recipes import recipe_ns
from auth import auth_ns
from flask_cors import CORS
import os
from decouple import config

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR, 'dev.db')
    app.config["SECRET_KEY"]=config('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    CORS(app)

    db.init_app(app)

    migrate=Migrate(app,db)
    JWTManager(app)

    api=Api(app,doc='/docs')

    api.add_namespace(recipe_ns)
    api.add_namespace(auth_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "Recipe": Recipe,
            "user":User
        }

    return app