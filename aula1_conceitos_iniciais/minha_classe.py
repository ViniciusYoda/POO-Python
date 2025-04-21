class MinhaClasse:
    def __init__(self, info, elem):
        self.atributo_1 = 'meu atributo 1'
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, 3]
        self.new_atributo = info
        print(self.new_atributo)

    def metodo_1(self):
        print('minha ação 1')
        print('minha ação 2')
        return 'Olá mundo'

    def metodo_2(self, numero):
        print(self.atributo_3[1] + numero)

minha_classe = MinhaClasse('info aqui no construtor',213)

response = minha_classe.metodo_1()
print(response)
minha_classe.metodo_2(10)