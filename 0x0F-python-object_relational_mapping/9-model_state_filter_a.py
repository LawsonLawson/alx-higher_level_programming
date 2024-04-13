#!/usr/bin/python3
'''
A module that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
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
    db_session = SessionMaker()

    # Query State objects containing the letter 'a' in their name
    states_with_letter_a = db_session.query(State).filter(State.name
                                                          .contains("a"))

    # Print the results
    for state in states_with_letter_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    db_session.close()
