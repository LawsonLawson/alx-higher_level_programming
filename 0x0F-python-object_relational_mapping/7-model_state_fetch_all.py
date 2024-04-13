#!/usr/bin/python3
'''
This module lists all State objects from the database hbtn_0e_6_usah
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
    session = SessionMaker()

    # Query all State objects
    all_states = session.query(State).all()

    # Print the results
    for state in all_states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
