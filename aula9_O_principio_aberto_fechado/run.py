class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f'O {self.tipo} está se apresentando!')

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print(f'O show está começando!')
        artista.apresentar_show()
        print(f'O show do {artista.tipo} terminou!')

circo = Circo()
palhaço = Artista('palhaço')
mestre = Artista('mestre de cerimônias')

circo.apresentar(palhaço)
circo.apresentar(mestre)