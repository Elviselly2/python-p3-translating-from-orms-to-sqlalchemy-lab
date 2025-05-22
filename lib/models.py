from sqlalchemy.orm import registry
from sqlalchemy import Column, Integer, String

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Dog(Base):
    __tablename__ = 'dogs'  # Define the table name
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String)  # Name column
    breed = Column(String)  # Breed column
