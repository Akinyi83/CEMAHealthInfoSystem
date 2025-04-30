from flask import Blueprint, jsonify, request, render_template,redirect, url_for
from .models import get_all_clients, add_client, add_health_program, add_enrollment, get_all_enrollments, get_clients_with_programs, get_client_by_id
from app.models import get_all_health_programs 
#from app.db import get_db_connection

client_routes = Blueprint('client_routes', __name__)


# Dashboard for viewing all clients
@client_routes.route('/client', methods=['GET'])
def dashboard():
    clients = get_clients_with_programs() #get_all_clients()
    return render_template('dashboard.html', clients=clients)

# API endpoint to get all clients
@client_routes.route('/client/json', methods=['GET'])
def api_get_clients():
    clients = get_all_clients()
    return jsonify(clients), 200


# API endpoint to add a new client
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

# View a specific client's profile
@client_routes.route('/client/<int:client_id>', methods=['GET'])
def client_profile(client_id):
    client = get_client_by_id(client_id)  # You need to implement or import this
    if client:
        return render_template('client_profile.html', client=client)
    else:
        return "Client not found", 404



@client_routes.route('/client/search', methods=['GET', 'POST'])
def search_client():
    
    if request.method == 'POST':
        query = request.form.get('search_query', '')

        all_clients = get_all_clients()
        all_enrollments = get_all_enrollments()
        all_programs = get_all_health_programs()
        print("DEBUG: all_enrollments =", all_enrollments)

        # Build a mapping: program_id -> program_name
        program_dict = {program['id']: program['program_name'] for program in all_programs}

        results = []

        for client in all_clients:
            if (query.lower() in client['first_name'].lower() or
                query.lower() in client['last_name'].lower() or
                query.lower() in client['email'].lower()):
                
                # Find the programs this client is enrolled in
                client_programs = []
                for enrollment in all_enrollments:
                    if str(enrollment.get('client_id')) == str(client['id']):
                        program_name = program_dict.get(enrollment.get('program_id'), "Unknown Program")
                        if program_name not in client_programs:
                            client_programs.append(program_name)

                # Add programs to client info
                client_with_programs = {
                    'id': client['id'],
                    'first_name': client['first_name'],
                    'last_name': client['last_name'],
                    'email': client['email'],
                    'programs': client_programs
                }

                results.append(client_with_programs)

        return render_template('search_results.html', query=query, results=results)

    # For GET request: just show the empty search form!
    return render_template('search_client_form.html')



# API endpoint to create health programs (single or list)
@client_routes.route('/health_program/create', methods=['GET', 'POST'])
def create_health_program():
    if request.method == 'GET':
        return render_template('create_health_program.html')  # Create a simple form to create program

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    program_name = data.get('program_name')
    description = data.get('description')

    if not program_name:
        return jsonify({"error": "Program name is required"}), 400

    add_health_program(program_name, description)
    return jsonify({"message": "Health program created successfully"}), 201

#@client_routes.route('/health_program/create', methods=['GET','POST'])
#def create_health_program():
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
    
    

# API endpoint to get all health programs
@client_routes.route('/programs/json', methods=['GET'])
def api_get_health_programs():
    programs = get_all_health_programs()
    return jsonify(programs), 200

# New route for enrolling a client in a health program
@client_routes.route('/enrollments', methods=['GET', 'POST'])
def create_enrollment():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            client_id = data.get('client_id')
            program_id = data.get('program_id')
        else:
            client_id = request.form.get('client_id')
            program_id = request.form.get('program_id')

            if client_id and program_id:
                try:
                   add_enrollment(client_id, program_id)
                   if request.is_json:
                       return "Enrollment successful", 201
                   else:
                       return "Enrollment successful"
                except Exception as e:
                    if request.is_json:
                        return f"Enrollment failed: {str(e)}", 500
                    else:
                        return f"Enrollment failed: {str(e)}"
            else:
                    if request.is_json:
                        return "Missing client_id or program_id", 400
                    else:
                        return "Missing client_id or program_id"
    else:
        #Render form for enrolling client
        clients = get_all_clients()
        programs = get_all_health_programs()
        return render_template('enroll_client.html', clients=clients, programs=programs)

@client_routes.route('/enrollments/json', methods=['GET'])
def api_get_enrollments():
    enrollments = get_all_enrollments()
    return jsonify(enrollments), 200


#create client route to Register new client
@client_routes.route('/clients/new', methods=['GET', 'POST'])
def create_client():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        add_client(first_name, last_name, email)  # Call your models.py function
        return redirect(url_for('client_routes.dashboard'))
    
    return render_template('register_client.html')

