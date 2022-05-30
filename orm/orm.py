from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connection import Connection


con = Connection().str_connection()
engine = create_engine(con, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user = Column(String(10))
    password = Column(String(5))

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    categoria = Column(String(20))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    produto = Column(String(30))
    id_categoria = Column(Integer, ForeignKey('categorias.id'))

Base.metadata.create_all(engine)