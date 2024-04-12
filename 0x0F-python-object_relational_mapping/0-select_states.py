#!/usr/bin/python3
"""
Task 0:
0-select_states.py
Lists all states from the database hbtn_0e_0_usa

Dependencies:
0-select_states.sql
"""
from sys import argv
import MySQLdb


def main():
    """
    Connects to the MySQL database and lists all states.
    """
    # Retrieve command line arguments
    mysql_user = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id;")

    # Fetch all rows
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
