#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import insert
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()