import os
from sqlalchemy import create_engine, exc, text

def ensure_database_exists(database_name):
    temp_engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/')
    try:
        # Connect to the MySQL server directly, not any specific database
        with temp_engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
            print(f"Database '{database_name}' ensured or created.")
    except exc.SQLAlchemyError as e:
        print(f"An error occurred while ensuring/creating the database: {e}")


USERNAME = os.getenv('DBUSERNAME')
PASSWORD = os.getenv('DBPASSWORD')
DATABASE = 'OPTIONSDATA'
HOSTNAME = os.getenv('HOSTNAME')
PORT = 3306  # Default MySQL port

ensure_database_exists(DATABASE)

# Engine for regular use
ENGINE = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}')