class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self,qtd):
        if qtd <= 0:
            print("Quantidade inválida")
        else:
            self.quantidade += qtd
            print(f"Adicionado {qtd} unidades. Estoque atual: {self.quantidade}")

    def vender(self, qtd):
        if qtd > self.quantidade:
            print ("Estoque insuficiente")

        elif qtd <= 0:
            print("Quantidade inválida")

        else:
            self.quantidade -= qtd
            print(f"Vendido {qtd} unidades. Estoque atual: {self.quantidade}")

    def valor_total_estoque(self):
        return self.preco * self.quantidade

    def mostrar_info(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.quantidade} unidades")

        
produto = Produto("Caneta", 2.50, 100)
produto.mostrar_info()
produto.adicionar_estoque(50)
produto.vender(30)
produto.vender(1000)
produto.adicionar_estoque(-5)
produto.mostrar_info()
print(f"Valor total em estoque: R${produto.valor_total_estoque()}")