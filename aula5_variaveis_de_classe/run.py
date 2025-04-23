class MinhaClasse:
    estatico = "lhama"
    def __init__(self, estado) -> None:
        self.__estado = estado
        print(self.__estado)

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "cachorro"
obj1.estatico = "gato"
obj2.estatico = "cavalo"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)