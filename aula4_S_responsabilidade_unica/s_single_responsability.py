class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__error_handle()

    def __validate_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
        
    def __register_user(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print(f"Cadastrando {nome} com idade {idade}.")

    def __error_handle(self) -> None:
        print('Erro: Nome deve ser uma string e idade deve ser um inteiro.')    

sistema = SistemaCadastral()
sistema.cadastrar('Lucas', 25)  # Saída: Acessando o banco de dados... Cadastrando Lucas com idade 25.
sistema.cadastrar(123, 'vinte e cinco')  # Saída: Erro: Nome deve ser uma string e idade deve ser um inteiro.
