class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None

    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    @property
    def getter_valor(self) -> int:
        return self.__valor

my_class = MinhaClasse()
my_class.setter_valor(10)
print(my_class.getter_valor)  # Saída: 10
# my_class.getter_valor = 20  # Isso causará um erro, pois getter_valor é somente leitura
# my_class.getter_valor()  # Isso causará um erro, pois getter_valor é somente leitura
