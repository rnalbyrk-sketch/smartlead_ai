import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "gelistirme-icin-gecici-anahtar")
    DATABASE_URL = os.environ.get("DATABASE_URL", "leads.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "demo")

    BUSINESS_CONTEXT = """
    SESİZ, görme engelli ve az gören bireylerin günlük yaşamını
    kolaylaştırmayı amaçlayan bir yapay zekâ asistanı projesidir.
    Ürün hakkında bilgi ver, ziyaretçilerin sorularını yanıtla.
    Bilmediğin özellikleri varmış gibi anlatma.
    """

    CORS_ORIGINS = os.environ.get(
    "CORS_ORIGINS",
    "http://localhost:5000,https://rnalbyrk.wixsite.com"
).split(",")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
