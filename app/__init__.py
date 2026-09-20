from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_cors import CORS

from config import DevelopmentConfig
from app.database import init_db
from app.routes import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    CORS(app, origins=app.config["CORS_ORIGINS"])
    init_db(app)
    app.register_blueprint(main_bp)

    return app