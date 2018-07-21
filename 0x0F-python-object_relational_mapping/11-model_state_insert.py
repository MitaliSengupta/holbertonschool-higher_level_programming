#!/usr/bin/python3
"""
Script that adds the state obj "Louisiana" to the db
takes 3 args
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
    st = State(name="Louisiana")
    session().add(st)
    for stat in session().query(State).filter(
            State.name == 'Louisiana').order_by(State.id).all():
        if stat:
            print(stat.id)
    session().commit()
    session().close()
