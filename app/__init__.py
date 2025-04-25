from flask import Flask
import mysql.connector
from .routes import client_routes  # Import routes from routes.py

def create_app():
    app = Flask(__name__)

    # MySQL connection details
    app.config['DB_HOST'] = 'localhost'
    app.config['DB_USER'] = 'root'  # Replace with your MySQL username
    app.config['DB_PASSWORD'] = 'your_password'  # Replace with your MySQL password
    app.config['DB_NAME'] = 'cemahealth_info_system'

    # Register Blueprints
    app.register_blueprint(client_routes, url_prefix='/api')  # Use /api prefix for your routes

    return app
from flask import Flask
import mysql.connector
from .routes import client_routes  # Import routes from routes.py

def create_app():
    app = Flask(__name__)

    # MySQL connection details
    app.config['DB_HOST'] = 'localhost'
    app.config['DB_USER'] = 'root'  # Replace with your MySQL username
    app.config['DB_PASSWORD'] = 'password'  # Replace with your MySQL password
    app.config['DB_NAME'] = 'cemahealth_info_system'

    # Register Blueprints
    app.register_blueprint(client_routes, url_prefix='/api')  # Use /api prefix for your routes

    return app
