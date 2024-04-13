#!/usr/bin/python3
'''
Module for listing all cities of a specific state, using the database
hbtn_0e_4_usa
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    # Retrieve MySQL connection details and state name from cmd line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # SQL query to select all cities of a specific state
    sql_query = """
                SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id
                """

    # Execute the SQL query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Extract city names from the results and print them
    city_names = [state_record[0] for state_record in result_set]
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    connection.close()
