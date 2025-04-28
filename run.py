from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
