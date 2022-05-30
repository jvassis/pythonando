from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connection import Connection

engine = create_engine(Connection().str_connection())
session = sessionmaker(bind=engine)()
Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    user = Column(String(20))
    email = Column(String(100))
    password = Column(String(100))

Base.metadata.create_all(engine)