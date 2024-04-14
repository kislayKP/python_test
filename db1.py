import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='student'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create a new database
            db_name = 'ki'
            cursor.execute(f"CREATE DATABASE {db_name}")
            print("Database created successfully.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

