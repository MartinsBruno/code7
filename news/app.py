from flask import Flask

from news.extensions import config
from news.extensions.database import mongo

from news.blueprints import api

def create_app():
    """Main Factory"""
    app = Flask(__name__)
    config.init_app(app)
    mongo.init_app(app)

    api.init_app(app)
    return app