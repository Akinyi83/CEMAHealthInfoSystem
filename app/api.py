from flask import Blueprint, jsonify, request, render_template
from .models import get_all_clients, add_client

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/')
def dashboard():
    clients = get_all_clients()
    return render_template('dashboard.html', clients=clients)

@api_routes.route('/clients', methods=['GET'])
def api_get_clients():
    clients = get_all_clients()
    return jsonify(clients), 200

@api_routes.route('/clients', methods=['POST'])
def api_add_client():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')

    if first_name and last_name and email:
        try:
            add_client(first_name, last_name, email)
            return jsonify({'message': 'Client added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Missing data: first_name, last_name, and email are required'}), 400
