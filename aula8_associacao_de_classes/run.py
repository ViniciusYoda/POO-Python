class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self) -> None:

        print(f'Acendendo o interruptor do {self.comodo}')

    def apagar(self) -> None:
        print(f'Apagando o interruptor do {self.comodo}')

class Pessoa:
    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()

    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print('Dormindo...')    


interruptor_quarto = Interruptor('quarto')
interruptor_sala = Interruptor('sala')
pessoa = Pessoa()
pessoa.acender_luzes(interruptor_quarto)
pessoa.apagar_luzes(interruptor_quarto)
pessoa.acender_luzes(interruptor_sala)
pessoa.apagar_luzes(interruptor_sala)
pessoa.dormir()
