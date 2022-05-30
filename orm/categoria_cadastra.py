from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Categoria
from connection import Connection


con = Connection().str_connection()
engine = create_engine(con, echo=False)
session = sessionmaker(bind=engine)()

categorias = [
    Categoria(categoria='frios'),
    Categoria(categoria='frutas')
]

session.add_all(categorias)
session.commit()