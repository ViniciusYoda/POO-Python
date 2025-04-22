class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print(f"Cadastrando {nome} com idade {idade}.")
        else:
            print('Erro: Nome deve ser uma string e idade deve ser um inteiro.')