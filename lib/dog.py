from models import Dog
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()

# Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'  # Define the table name
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String)  # Name column
    breed = Column(String)  # Breed column

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()  # Fixed for compatibility

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()