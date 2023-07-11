import pytest
from src.etl import run_etl
from src.db_handler import get_db_connection

def test_etl():
    # Run the ETL process
    run_etl()

    # Validate the data ended up in the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM user_logins')
    count = cur.fetchone()[0]
    assert count > 0, "No data found in 'user_logins' table"

    cur.close()
    conn.close()
