import os
from flask import Flask
from dotenv import load_dotenv

from Library.routes import pages

load_dotenv()


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )

    app.register_blueprint(pages)

    return app
