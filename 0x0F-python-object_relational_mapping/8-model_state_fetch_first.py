#!/usr/bin/python3
'''
This module prints the first State object from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Retrieve MySQL connection details from command line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create the database engine
    database_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                    .format(mysql_username, mysql_password,
                                            database_name), pool_pre_ping=True)

    # Create a sessionmaker
    SessionMaker = sessionmaker(database_engine)

    # Create a session
    database_session = SessionMaker()

    # Query the first State object
    first_state_object = database_session.query(State).first()

    # Print the result
    if first_state_object is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state_object.id, first_state_object.name))

    # Close the session
    database_session.close()
