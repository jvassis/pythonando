from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'mensagem': 'hello world!'}

@app.get('/cadastro')
def cadastro():
    return {'mensagem': 'cadastro'}

@app.get('/login')
def cadastro():
    return {'mensagem': 'login'}

# execute no terminal
# uvicorn main:app --reload