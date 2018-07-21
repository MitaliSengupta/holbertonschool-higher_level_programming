#!/usr/bin/python3
"""
Script that prints all city obj
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import aliased, sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    res = (session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all())
    for st, cy in res:
        print("{}: ({:d}) {}".format(st.name, cy.id, cy.name))
    session.close()
