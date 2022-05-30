from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Pessoa
from connection import Connection


con = Connection().str_connection()
engine = create_engine(con, echo=False)
session = sessionmaker(bind=engine)()

# pessoa = Pessoa(
#     name='caio',
#     user='caio',
#     password='caio'
# )

# session.add(pessoa)
# session.commit()

pessoas = [
    Pessoa(
        name='joao',
        user='joao',
        password='joao'
    ),
    Pessoa(
        name='jose',
        user='jose',
        password='jose'
    )
]

session.add_all(pessoas)
# session.rollback() # limpeza da session
session.commit()