from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://postgres:password@localhost:5432/postgres"

db = create_engine(db_string)
base = declarative_base()


class Customer(base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone_number = Column(String(255))
    email = Column(String(255))


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
