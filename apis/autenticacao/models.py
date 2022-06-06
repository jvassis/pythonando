from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


USER = 'root'
PASSWORD = 'root'
HOST = 'localhost'
DB = 'fastapi'
PORT = 3306
CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONN, echo=True)
session = sessionmaker(bind=engine)()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user = Column(String(20))
    password = Column(String(10))

class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow())

Base.metadata.create_all(engine)