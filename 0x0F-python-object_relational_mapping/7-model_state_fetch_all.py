#!/usr/bin/python3
"""
script that lists all state objects from the
db takes 3 args result needs to be sorted
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for st in session().query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
    session().close()
