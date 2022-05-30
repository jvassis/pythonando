from socket import socket, AF_INET, SOCK_STREAM


HOST = 'localhost'
PORT = 8002

sk = socket(AF_INET, SOCK_STREAM)
sk.connect((HOST, PORT))

sk.send(input('digite o nome do arquivo: ').encode())
file = open('client-files/image.png', 'rb')
sk.send(file.read())

res = sk.recv(1024)
print(res)