from app.models import get_all_clients, add_client
from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Use environment variables
app.config['DB_HOST'] = os.getenv('DB_HOST')
app.config['DB_USER'] = os.getenv('DB_USER')
app.config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['DB_NAME'] = os.getenv('DB_NAME')

with app.app_context():
    print("Fetching all clients:")
    clients = get_all_clients()
    for client in clients:
        print(client)

    # Uncomment to test adding a new client
    # add_client("Vallary Ogolla", "vallary@example.com", "0725678")
