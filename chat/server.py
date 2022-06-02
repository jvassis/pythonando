from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


HOST = '127.0.0.1'
PORT = 55555

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcast(sala, mensagem):
    for client in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        client.send(mensagem)

def enviar_mensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f'{nome}: {mensagem.decode()}\n'
        broadcast(sala, mensagem)

while True:
    client, address = server.accept()
    client.send(b'sala')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f'{nome} se conectou na sala {sala}! info {address}')
    broadcast(sala, f'{nome}: entrou na sala!\n')
    thread = Thread(
        target=enviar_mensagem,
        args=(nome, sala, client)
    ).start()