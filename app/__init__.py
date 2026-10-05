from flask import Flask
from flask_cors import CORS
from config import Config
from app.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config["CORS_ORIGINS"] = "*"
    app.config["CORS_RESOURCES"] = r"/.*"

    CORS(app)

    # Veritabanında leads tablosu yoksa oluşturur.
    init_db(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
