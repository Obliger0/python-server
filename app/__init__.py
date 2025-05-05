from flask import Flask
from .routes import main
from flask_cors import CORS
from .db import init_db
from dotenv import load_dotenv
load_dotenv()

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)

    # Load default and instance config
    app.config.from_object('app.config.Config')
    app.config.from_pyfile('config.py', silent=True)

    CORS(app)
    app.register_blueprint(main)

    return app

print("Server running...")

init_db()

print("Database initialized.")