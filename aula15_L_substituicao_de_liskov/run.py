class Animal:
    def alimentar(self):
        print("Animal alimentado")

class Cachorro(Animal):

    def latir(self):
        print("Cachorro latindo")

class Peixe(Cachorro):
    def nadar(self):
        print('O Peixe está nadando')

    def latir(self):
        raise Exception("Peixe não pode latir")
    
def verificar_animal(animal: any):
    animal.latir()

obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()

verificar_animal(obj1) 
verificar_animal(obj2)  
verificar_animal(obj3) 