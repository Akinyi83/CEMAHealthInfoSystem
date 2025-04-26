from flask import Flask
import os
from dotenv import load_dotenv
from .routes import client_routes

def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # MySQL connection details
    app.config['DB_HOST'] = os.getenv('DB_HOST')
    app.config['DB_USER'] = os.getenv('DB_USER')
    app.config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
    app.config['DB_NAME'] = os.getenv('DB_NAME')

    # Register Blueprints
    app.register_blueprint(client_routes, url_prefix='/api')

    return app
