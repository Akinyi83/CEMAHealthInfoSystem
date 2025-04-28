from flask import current_app, g
import mysql.connector

def get_db():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(
                host=current_app.config['DB_HOST'],
                user=current_app.config['DB_USER'],
                password=current_app.config['DB_PASSWORD'],
                database=current_app.config['DB_NAME']
            )
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            raise
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_all_clients():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clients")
    result = cursor.fetchall()
    cursor.close()
    return result

def add_client(first_name, last_name, email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s)",
        (first_name, last_name, email)
    )
    db.commit()
    cursor.close()

def add_health_program(program_name, description):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO health_programs (program_name, description) VALUES (%s, %s)",
        (program_name, description)
    )
    db.commit()
    cursor.close()

 # endpoint to list all health programs  
def get_all_health_programs():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM health_programs")
    programs = cursor.fetchall()
    cursor.close()
    return programs

# Add a new enrollment
def add_enrollment(client_id, program_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO enrollments (client_id, program_id) VALUES (%s, %s)",
        (client_id, program_id)
    )
    db.commit()
    cursor.close()

# Get all enrollments
def get_all_enrollments():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT enrollments.id, clients.first_name, clients.last_name, health_programs.program_name
        FROM enrollments
        JOIN clients ON enrollments.client_id = clients.id
        JOIN health_programs ON enrollments.program_id = health_programs.id
    """)
    enrollments = cursor.fetchall()
    cursor.close()
    return enrollments
