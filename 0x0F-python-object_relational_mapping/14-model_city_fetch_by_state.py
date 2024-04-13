#!/usr/bin/python3
'''
This is a module that that prints all City objects from the database
hbtn_0e_14_usa
'''


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

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

    # Query all City objects and their corresponding State objects
    city_state_pairs = db_session \
        .query(City, State).filter(State.id == City.state_id) \
        .order_by(City.id).all()

    # Print the results
    for city, state in city_state_pairs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    db_session.close()
