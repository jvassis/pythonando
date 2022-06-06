from sqlalchemy import create_engine
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from models import CONN, Pessoa, Token
from secrets import token_hex


app = FastAPI()

def conecta_db():
    engine = create_engine(CONN, echo=True)
    return sessionmaker(bind=engine)()

@app.post('/cadastro')
def main(name: str, user: str, password: str):
    session = conecta_db()
    user_ = session.query(Pessoa).filter_by(user=user, password=password).one()
    if not user_:
        user_ = Pessoa(name=name, user=user, password=password)
        session.add(user_)
        session.commit()
        return {'status': 'usuario cadastrado com sucesso'}
    else:
        return {'status': 'usuario ja cadastrado'}

@app.post('/login')
def main(user: str, password: str):
    session = conecta_db()
    user_ = session.query(Pessoa).filter_by(user=user, password=password).one()
    if not user_:
        return {'status': 'usuario inexistente'}
    while True:
        token = token_hex(50)
        token_ = session.query(Token).filter_by(token=token).one()
        if not token_:
            user_token = session.query(Token).filter_by(id_pessoa=user_.id).one()
            if not user_token:
                new_token = Token(id_pessoa=user_.id, token=token)
                session.add(new_token)
            else:
                user_token.token = token
            session.commit()
            break
    return token
