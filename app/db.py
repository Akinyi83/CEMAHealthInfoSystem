import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',       # or your DB server address
        user='your_mysql_user', # your MySQL username
        password='your_password', # your MySQL password
        database='cema_health_system'
    )
    return conn
