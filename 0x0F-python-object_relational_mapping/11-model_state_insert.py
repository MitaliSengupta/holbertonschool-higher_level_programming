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
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    st = State(name="Louisiana")
    session.add(st)
    session.commit()
    print(st.id)
    session.close()
