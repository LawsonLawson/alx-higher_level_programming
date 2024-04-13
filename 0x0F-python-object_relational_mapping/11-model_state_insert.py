#!/usr/bin/python3
'''
This module adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # Create a new State object
    new_state = State()
    new_state.name = "Louisiana"

    # Add the new State object to the session
    db_session.add(new_state)

    # Commit the changes to the database
    db_session.commit()

    # Print the ID of the newly added State object
    print("{}".format(new_state.id))

    # Close the session
    db_session.close()
