from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Pessoa
from connection import Connection


con = Connection().str_connection()
engine = create_engine(con, echo=False)
session = sessionmaker(bind=engine)()

pessoas = session.query(Pessoa).filter(Pessoa.id == 1).all()
pessoas[0].name = 'joao da silva'

session.commit()