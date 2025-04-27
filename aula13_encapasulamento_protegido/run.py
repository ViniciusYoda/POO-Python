class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f'O animal está andando pelo {self.localizacao}')

    def _dormir(self) -> None:
        print('O animal está dormindo')

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print('O animal está miando')
        self.andar()
        self._dormir()
        print(f'O tamanho do gato é {self._tamanho}')

cat = Gato('Arge')
cat.miar()
cat._dormir()  # Acesso permitido, mas não recomendado
cat.andar()  # Acesso permitido, mas não recomendado
print(cat._tamanho)  # Acesso permitido, mas não recomendado