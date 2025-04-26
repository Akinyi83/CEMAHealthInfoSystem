from flask import Flask
import mysql.connector
from .routes import client_routes

def create_app():
    app = Flask(__name__)

    # MySQL connection details
    app.config['DB_HOST'] = 'localhost'
    app.config['DB_USER'] = 'root'  # Replace if needed
    app.config['DB_PASSWORD'] = 'password' \
    ''  # Replace if needed
    app.config['DB_NAME'] = 'cema_health_system'  #  Updated database name

    # Register Blueprints
    app.register_blueprint(client_routes, url_prefix='/api')

    return app
