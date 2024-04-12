#!/usr/bin/python3

'''
This script retrieves and displays all states from the hbtn_0e_0_usa database.
'''

import sys
import MySQLdb

if __name__ == '__main__':

    # Connect to the MySQL database
    db_connection = MySQL.connect(user=sys.argv[1], passwd=sys.argv[2],
                                  db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    db_cursor = db_connection.cursor()

    # Execute the SQL query to retrieve all states
    db_cursor.execute("SELECT * FROM states;")

    # Fetch all the rows returned by the query
    states_data = db_cursor.fetchall()

    # Display each state
    for state_record in states_data:
        print(state_record)
