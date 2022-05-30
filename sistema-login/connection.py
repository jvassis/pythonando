from pathlib import Path

path_arq = Path().cwd().joinpath('db', 'login.sqlite')

class Connection:
    def str_connection(self):
        return f'sqlite:///{path_arq}'