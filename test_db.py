from app.models import get_all_clients, add_client
from flask import Flask

app = Flask(__name__)
app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = 'password'
app.config['DB_NAME'] = 'cema_health_system'

with app.app_context():
    print("Fetching all clients:")
    clients = get_all_clients()
    for client in clients:
        print(client)

    # Uncomment to test adding a new client
    # add_client("Vallary Ogolla", "vallary@example.com", "0725678")
