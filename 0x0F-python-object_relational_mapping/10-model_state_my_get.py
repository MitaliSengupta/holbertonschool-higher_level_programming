#!/usr/bin/python3
"""
script that prints the state obj with the name
passed as arg from the db
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    st = session().query(State).filter(State.name == argv[4]).all()
    if st:
        for stat in st:
            if stat.name == argv[4]:
                print("{}".format(stat.id))
    else:
        print("Not found")
    session().close()
