#Exercício: Classe Pessoa

class Pessoa:
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Oi, meu nome é {self.nome} e eu tenho {self.idade} anos"

    def fazer_aniversario(self):
        self.idade +=1

pessoa1 = Pessoa("Vitor", 20)

print(pessoa1.apresentar())

pessoa1.fazer_aniversario()
print(pessoa1.apresentar())