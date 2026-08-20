import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@DIT121death",  # <--- Make sure this matches your MySQL password
            database="bank_management"
        )
        if connection.is_connected():
            return connection

    except Error as e:
        print(f"Database connection error: {e}")
        return None