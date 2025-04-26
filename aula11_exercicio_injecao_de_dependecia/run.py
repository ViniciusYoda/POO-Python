class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_banco(self) -> None:
        self.connection = True

class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1,2,3,4,5]

        return None
    
class RegraDeNegocio:
    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print('Dados não encontrados verifique sua conexão com o Banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'O resultado é: {resposta}')

conn = ConectorBancoDeDados()
conn.conectar_ao_banco()

repo = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repo)

regra.calcular_resultados()