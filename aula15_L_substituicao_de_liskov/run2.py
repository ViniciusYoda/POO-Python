class ConnectDB:
    def conectar(self):
        print('Conectando ao banco de dados...')

class SqlRepository(ConnectDB):
    def select(self):
        print('Selecionando dados...')

class NoSQLRepository(ConnectDB):
    def select(self):
        print('Selecionando dados...')  

class DBHandler:
    def alterTable(self):
        print('Alterando tabela...')
