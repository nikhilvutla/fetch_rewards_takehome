import psycopg2
from .config import POSTGRES_CONFIG

def get_db_connection():
    conn = psycopg2.connect(**POSTGRES_CONFIG)
    return conn

def insert_data(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    # write the insert query
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
