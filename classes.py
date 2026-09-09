#criando minha primeira classe!

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        return"Au, Au"

    def comer(self):
        return"gosta de comer muito"

cachorro1 = Cachorro("Rex", 3)
cachorro2 = Cachorro("Bob", 5)
cachorro3 = Cachorro("Thor", 7)

print(f"O meu cachorro se chama {cachorro1.nome},tem {cachorro1.idade} anos e faz {cachorro1.latir()}")
print(f"O meu cachorro se chama {cachorro2.nome},tem {cachorro2.idade} anos e também faz {cachorro2.latir()}")
print (f"O meu cachorro se chama {cachorro3.nome}, tem {cachorro3.idade} anos e {cachorro3.comer()}")

animal = [cachorro1.nome , cachorro1.idade , cachorro1.comer()]

print (f"estou doando esse cachorro: \n{animal},\n podem pegar!")


