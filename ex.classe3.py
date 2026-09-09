class Produto:
    def __init__(self, nome, preço, estoque=20):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

    def vender(self,quantidade):

        if quantidade > self.estoque:
            print ("estoque insuficiente")
        else:
            self.estoque -= quantidade
            print(f"Vendido: {quantidade}")

    def repor(self, quantidade):
        self.estoque += quantidade

    def info(self):
        return f"{self.nome} {self.preço}  {self.estoque}"

produto1 = Produto("Caneta" , 2.5, 7 )

print(f"Produto: {produto1.nome} \nPreço R$:{produto1.preço} \nEstoque:{produto1.estoque}")


