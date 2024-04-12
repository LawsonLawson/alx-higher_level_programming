#!/usr/bin/python3

'''
This script retrieves and displays all states from the hbtn_0e_0_usa database.
'''

import sys
import MySQLdb

def main():
    # Extract the command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1:]

    # Connect to the MySQL database
    db_connection = MySQL.connect(
            host="localhost",
            user=mysql_username,
            password=mysql_password,
            database=db_name,
            port=3306,
            )

    # Create a cursor object to interact with the database
    db_cursor = db_connection.cursor()

    # Execute the SQL query to retrieve all states
    db_cursor.execute("SELECT * FROM states ORDER BY states.id;")

    # Fetch all the rows returned by the query
    states_data = db_cursor.fetchall()

    # Display each state
    for state_record in states_data:
        print(state_record)

    # Close the cursoer and connection
    db_cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
