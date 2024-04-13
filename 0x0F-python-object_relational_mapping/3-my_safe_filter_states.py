#!/usr/bin/python3
'''
Module for displaying all values in the states table of hbtn_0e_0_usa
where name matches the argument.
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    # Retrieve MySQL connection details and search argument from cmd line args
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search_argument = sys.argv[4]

    # Connect to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # SQL query to select states where name matches the search argument
    sql_query = """
    SELECT * FROM states WHERE
    name LIKE BINARY %s ORDER
    BY id ASC
    """

    # Execute the SQL query with the search argument
    cursor.execute(sql_query, (search_argument,))

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Print the results
    for state_record in result_set:
        print(state_record)

    # Close cursor and database connection
    cursor.close()
    connection.close()
