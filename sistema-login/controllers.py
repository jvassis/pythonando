import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connection import Connection
from models import User

def estabelece_session():
    engine = create_engine(Connection().str_connection(), echo=False)
    session = sessionmaker(bind=engine)()
    return session

class CadastroController:
    @classmethod
    def verifica_dados(cls, user, email, password):
        if len(user) > 20 or len(user) < 3:
            return 2
        if len(email) > 100:
            return 3
        if len(password) > 100 or len(password) < 4:
            return 4
        return 1 # flag de sucesso!
    @classmethod
    def cadastrar(cls, user, email, password):
        session = estabelece_session()
        users = session.query(User).filter(User.email == email).all()
        if len(users) > 0:
            return 5
        data_check = cls.verifica_dados(user, email, password)
        if data_check != 1:
            return data_check
        try:
            password = hashlib.sha256(password.encode()).hexdigest()
            user = User(user=user, email=email, password=password)
            session.add(user)
            session.commit()
            return 1 # flag de sucesso!
        except:
            return 6

class LoginController:
    @classmethod
    def login(cls, email, password):
        session = estabelece_session()
        password = hashlib.sha256(password.encode()).hexdigest()
        user = session.query(User).filter(User.email == email and User.password == password).one()
        if user:
            return {'logado': True, 'id': user.id}
        else:
            return False