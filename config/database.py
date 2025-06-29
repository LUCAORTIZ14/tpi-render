from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://tpidb:q1cPUwbJSXGkp0rnTvhwIzyIitcsKcOg@dpg-d1glg7idbo4c73avrtn0-a:5432/tienda"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
