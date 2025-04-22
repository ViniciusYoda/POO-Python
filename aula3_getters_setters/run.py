class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None

    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    def getter_valor(self) -> int:
        return self.__valor

my_class = MinhaClasse()
my_class.setter_valor(10)
print(my_class.getter_valor())  # Saída: 10