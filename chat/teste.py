from socket import socket, AF_INET, SOCK_STREAM


HOST = '127.0.0.1'
PORT = 55555

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)
print(mensagem)

if mensagem == b'sala':
    client.send(b'games')
    client.send(b'joao')