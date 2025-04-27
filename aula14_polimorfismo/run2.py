class ClasseQualquer:
    def fazer(self) -> None:
        print("Fazendo algo na classe qualquer")

class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print("Preparando algo na outra coisa")

def fazer_func() -> None:
        print("Fazendo algo diferente na outra coisa")

obj1 = ClasseQualquer()
obj2 = OutraCoisa()
obj2.fazer = fazer_func 

obj1.fazer()
obj2.fazer()
obj2.preparar()