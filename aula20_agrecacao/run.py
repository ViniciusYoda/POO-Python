class Produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome  
        self.__valor = valor

    def informacoes_do_produto(self) -> None:
        print(f'Produto: {self.__nome}')
        print(f'Valor: {self.__valor}')
        print('------------------')

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)
        
    def finalizar_compra(self) -> None:
        print('Compra finalizada!')
        print('Produtos no carrinho:')
        for produto in self.__produtos:
            produto.informacoes_do_produto()
        print('Obrigado pela compra!')

# Exemplo de uso
banana = Produto('Banana', 2)
maca = Produto('Maçã', 3)
laranja = Produto('Laranja', 4)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(banana)
carrinho.adicionar_produto(maca)
carrinho.adicionar_produto(laranja)

carrinho.finalizar_compra()



