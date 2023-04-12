from sqlalchemy import create_engine, Column, Integer, String
from models import Base
username = "serviceuser"
password = "servicepassword"
database = "healthrecord"

engine = create_engine(f'mysql://{username}:{password}@localhost/{database}')

Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_engine():
    return engine
