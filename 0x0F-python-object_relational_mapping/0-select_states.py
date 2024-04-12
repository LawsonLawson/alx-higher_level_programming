#!/usr/bin/python3

'''
Script to list all states from the database 'hbtn_0e_0_usa'
'''

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieve MySQL connection details from command line arguments
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Connect to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        password=mysql_password,
        database=database_name,
        port=3306,
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # SQL query to select all states
    sql_query = """
                SELECT * FROM states ORDER BY id;
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
