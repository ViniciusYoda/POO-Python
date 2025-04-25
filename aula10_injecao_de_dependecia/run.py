class Celular:
    def __init__(self, modelo: str, cor: str) -> None:
        self.modelo = modelo
        self.cor = cor

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f'Enviando mensagem: {mensagem}')

    def abrir_emails(self) -> None:
        print('Abrindo emails...')

    def abrir_youtube(self) -> None:
        print('Abrindo YouTube...')

class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print('Pedindo pizza...')
        self.__celular.enviar_mensagem('Quero uma pizza de calabresa!')

    def estudar(self) -> None:
        print('Estudando...')
        self.__celular.abrir_youtube()

    def trabalhar(self) -> None:
        print('Trabalhando...')
        self.__celular.abrir_emails()


android = Celular('Samsung Galaxy S21', 'preto')
iphone = Celular('iPhone 13', 'branco')

pessoa1 = Pessoa(android)
pessoa1.pedir_pizza()
pessoa1.estudar()
pessoa1.trabalhar()



