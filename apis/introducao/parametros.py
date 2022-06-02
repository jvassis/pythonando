from fastapi import FastAPI


app = FastAPI()

usuarios = [
    (1, 'joao', 'minha senha'),
    (2, 'marcela', 'minha senha 2'),
    (3, 'maria', 'minha senha 3')
]

@app.get('/usuario/{id}')
def main(id: int):
    for usuario in usuarios:
        if usuario[0] == id:
            return {'nome': usuario[1], 'senha': usuario[2]}
    return None

@app.post('/usuario')
def main(nome):
    for usuario in usuarios:
        if usuario[1] == nome:
            return usuario
    return None
