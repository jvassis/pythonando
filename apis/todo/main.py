from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date


app = FastAPI()

class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]

tarefas = []

@app.post('/inserir')
def main(todo: Todo):
    try:
        tarefas.append(todo)
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}

@app.post('/tarefas')
def main(opcao: int = 0):
    if opcao == 0:
        return tarefas
    if opcao == 1:
        return [tarefa for tarefa in tarefas if tarefa.realizada]
    if opcao == 2:
        return [tarefa for tarefa in tarefas if not tarefa.realizada]

@app.get('/tarefa')
def main(id: int):
    try:
        return tarefas[id]
    except:
        return {'status': 'erro'}

@app.post('/alterar')
def main(id: int):
    try:
        tarefas[id].realizada = not tarefas[id].realizada
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}

@app.post('/excluir')
def main(id: int):
    try:
        del tarefas[id]
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}
