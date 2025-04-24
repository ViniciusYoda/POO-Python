class Loja:
    taxa = 1.15
    def __init__(self, valor: float) -> None:
        self.valor_produto_bruto = valor

    def consultar_valor_do_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'valor do produto: {valor_produto:.2f}')

    @classmethod
    def editar_taxa_do_produto(cls, valor: float):
        cls.taxa = valor

loja_praia = Loja(100)
loja_praia.consultar_valor_do_produto()
loja_praia.editar_taxa_do_produto(1.2)
loja_praia.consultar_valor_do_produto()
loja_montanha = Loja(50)
loja_montanha.consultar_valor_do_produto()
loja_montanha.editar_taxa_do_produto(1.3)
loja_montanha.consultar_valor_do_produto()