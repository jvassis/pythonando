from socket import socket, AF_INET, SOCK_STREAM


HOST = 'localhost'
PORT = 8002

sk = socket(AF_INET, SOCK_STREAM)
sk.bind((HOST, PORT))
sk.listen(1)

while True:
    new_sk, _ = sk.accept()
    name = new_sk.recv(1024).decode()
    new_file = new_sk.recv(1024000)
    with open(f'server-files/{name}.png', 'wb') as file:
        file.write(new_file)
    file.close()
    new_sk.send(b'arquivo salvo com sucesso!')
