from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def consultar_beneficios(self) -> None:
        pass

class TrabalhadorTemporario(ABC):
    
        @abstractmethod
        def trabalhar(self) -> None:
            pass
    
        @abstractmethod
        def ir_para_casa(self) -> None:
            pass

class Professor(Trabalhador):

    def trabalhar(self) -> None:
        print("O professor está dando aula.")

    def ir_para_casa(self) -> None:
        print("O professor foi para casa.")

    def consultar_beneficios(self) -> None:
        print("O professor está consultando os benefícios.")

class ProfessorSubstituto(Professor):

    def trabalhar(self) -> None:
        print("O professor substituto está dando aula.")

    def ir_para_casa(self) -> None:
        print("O professor substituto foi para casa.")

print("Professor Substituto")
professor_substituto = ProfessorSubstituto()
professor_substituto.trabalhar()
professor_substituto.ir_para_casa()
