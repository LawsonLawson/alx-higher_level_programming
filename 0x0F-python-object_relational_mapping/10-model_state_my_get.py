#!/usr/bin/python3
'''
This is a module that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
'''


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Retrieve MySQL connection details and search argument from cmd line args
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name_searched = argv[4]

    # Variable to track if the state with the searched name is found
    state_found = False

    # Create the database engine
    database_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                    .format(mysql_username, mysql_password,
                                            database_name), pool_pre_ping=True)

    # Create a sessionmaker
    SessionMaker = sessionmaker(database_engine)

    # Create a session
    db_session = SessionMaker()

    # Query all State objects
    states = db_session.query(State).all()

    # Search for the State object with the given name
    for state in states:
        if name_searched == state.name:
            print("{}".format(state.id))
            state_found = True
            break

    # Print a message if the state with the searched name is not found
    if not state_found:
        print("Not found")

    # Close the session
    db_session.close()
