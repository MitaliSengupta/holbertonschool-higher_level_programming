#!/usr/bin/python3
"""
Script that prints the first state obj from the
db hbtn_0e_0_usa, takes 3 args
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
    st = session().query(State).first()
    if st:
        print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session().close()
