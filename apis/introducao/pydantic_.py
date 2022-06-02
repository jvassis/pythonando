from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: Optional[str]
    senha: str

@app.post('/usuario')
def main(usuario: Usuario):
    return usuario

usuarios = [
    Usuario(id=1, nome='joao', senha='minha senha'),
    Usuario(id=2, nome='marcela', senha='minha senha 2'),
    Usuario(id=3, nome='maria', senha='minha senha 3')
]

@app.get('/usuarios')
def main():
    return usuarios

@app.post('/usuarios/cadastrar')
def main(usuario: Usuario):
    usuarios.append(usuario)
    return 'usuario cadastrado com sucesso!'
