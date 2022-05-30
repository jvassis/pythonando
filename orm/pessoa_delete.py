from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from orm import Pessoa
from connection import Connection


con = Connection().str_connection()
engine = create_engine(con, echo=False)
session = sessionmaker(bind=engine)()

pessoa = session.query(Pessoa).filter(Pessoa.id == 12)
pessoa.delete()

# session.delete(pessoa) # erro

session.commit()