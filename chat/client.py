import tkinter
from tkinter import *
from tkinter import simpledialog
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


class Chat:
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 55555
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((HOST, PORT))
        login = Tk()
        login.withdraw()
        self.janela_carregada = False
        self.ativo = True
        self.nome = simpledialog.askstring(
            'nome', 'digite seu nome', parent=login
        )
        self.sala = simpledialog.askstring(
            'sala', 'digite a sala', parent=login
        )
        Thread(target=self.conecta).start()
        self.janela()
    
    def janela(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title('chat')
        self.caixa_texto = Text(self.root)
        self.caixa_texto.place(
            relx=.05, rely=.01, width=700, height=600
        )
        self.enviar_mensagem = Entry(self.root)
        self.enviar_mensagem.place(
            relx=.05, rely=.8, width=500, height=30
        )
        self.btn_enviar = Button(
            self.root, text='enviar', command=self.enviar_mensagem_servidor
        )
        self.btn_enviar.place(
            relx=.7, rely=.8, width=100, height=30
        )
        self.root.protocol('WM_DELETE_WINDOW', self.fechar)
        self.root.mainloop()
    
    def fechar(self):
        self.root.destroy()
        self.client.close()
    
    def conecta(self):
        while True:
            rec = self.client.recv(1024)
            if rec == b'sala':
                self.client.send(self.sala.encode())
                self.client.send(self.nome.encode())
            else:
                try:
                    self.caixa_texto.insert('end', rec.decode())
                except:
                    pass
    
    def enviar_mensagem_servidor(self):
        mensagem = self.enviar_mensagem.get()
        self.client.send(mensagem.encode())

Chat()