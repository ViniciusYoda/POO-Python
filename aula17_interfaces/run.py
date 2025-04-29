from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def horario_de_almoço(self) -> None:
        pass

class Professor(Trabalhador):

    def trabalhar(self) -> None:
        print("O professor está dando aula.")

    def ir_para_casa(self) -> None:
        print("O professor foi para casa.")

    def horario_de_almoço(self) -> None:
        print("O professor está no horário de almoço.")

class Engenheiro(Trabalhador):
    
        def trabalhar(self) -> None:
            print("O engenheiro está projetando algo.")
    
        def ir_para_casa(self) -> None:
            print("O engenheiro foi para casa.")
    
        def horario_de_almoço(self) -> None:
            print("O engenheiro está no horário de almoço.")

def comunicar_o_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print('Comunicar o trabalhador para ir para casa')
    trabalhador.horario_de_almoço()
    trabalhador.ir_para_casa()

p1 = Professor()
p2 = Engenheiro()

comunicar_o_trabalhador(p1)
comunicar_o_trabalhador(p2)