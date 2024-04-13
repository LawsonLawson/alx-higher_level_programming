#!/usr/bin/python3
'''
Module for listing all cities from the database hbtn_0e_4_usa
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieve MySQL connection details from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # SQL query to select all cities with their corresponding state names
    sql_query = """
                SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id;
                """

    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Print the results
    for state_record in result_set:
        print(state_record)

    # Close cursor and database connection
    cursor.close()
    connection.close()
