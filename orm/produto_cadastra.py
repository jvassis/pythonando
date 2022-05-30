from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Produto
from connection import Connection


con = Connection().str_connection()
engine = create_engine(con, echo=False)
session = sessionmaker(bind=engine)()

produtos = [
    Produto(produto='frango', id_categoria=1),
    Produto(produto='banana', id_categoria=2)
]

session.add_all(produtos)
session.commit()