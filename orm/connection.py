class Connection:
    def __init__(self):
        self.USER = 'USER'
        self.PASSWORD = 'PASSWORD'
        self.HOST = 'HOST'
        self.DB = 'DB'
        self.PORT = 'PORT'
    def str_connection(self):
        return f'mysql+pymysql://{self.USER}:{self.SENHA}@{self.HOST}:{self.PORT}/{self.DB}'