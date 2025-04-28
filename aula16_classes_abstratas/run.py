from abc import ABC, abstractmethod

class Pessoa(ABC):
    def correr(self):
        print('Correndo...')

    @abstractmethod
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print('Aula de Python')

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('Cozinhando...')

p1 = Professor()
p1.correr()
p1.trabalhar()

