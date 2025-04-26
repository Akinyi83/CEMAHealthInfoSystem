from flask import Blueprint, jsonify, request, render_template
from .models import get_all_clients, add_client, add_health_program
from app.models import get_all_health_programs 
#from app.db import get_db_connection

client_routes = Blueprint('client_routes', __name__)

@client_routes.route('/client', methods=['GET'])
def dashboard():
    clients = get_all_clients()
    return render_template('dashboard.html', clients=clients)

@client_routes.route('/client/json', methods=['GET'])
def api_get_clients():
    clients = get_all_clients()
    return jsonify(clients), 200

@client_routes.route('/client', methods=['POST'])
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
        return jsonify({'error': 'Missing data'}), 400

@client_routes.route('/programs', methods=['POST'])
def create_health_program():
    data = request.get_json()

    if isinstance(data, list):
        # It's a list of programs
        for program in data:
            program_name = program.get('program_name')
            description = program.get('description')

            if not program_name:
                return jsonify({"error": "Program name is required"}), 400

            add_health_program(program_name, description)

        return jsonify({"message": "Health programs created successfully"}), 201
    else:
        # Single program
        program_name = data.get('program_name')
        description = data.get('description')

        if not program_name:
            return jsonify({"error": "Program name is required"}), 400

        add_health_program(program_name, description)
        return jsonify({"message": "Health program created successfully"}), 201


@client_routes.route('/programs/json', methods=['GET'])
def api_get_health_programs():
    programs = get_all_health_programs()
    return jsonify(programs), 200


