import os
from flask import Flask
from dotenv import load_dotenv

from Library.routes import pages

load_dotenv()


def create_app(db_url=None):
    app = Flask(__name__)

    app.register_blueprint(pages)

    return app
