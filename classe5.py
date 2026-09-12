class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):

        if valor <= 0:
            print("Valor de depósito inválido")
        else:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")

    def sacar(self, valor):

        if valor > self.saldo:
            print("Saldo insuficiente")
        elif valor <= 0:
            print("Valor de saque inválido")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: {self.saldo}")


conta = ContaBancaria("Maria", 100)
conta.mostrar_saldo()
conta.depositar(50)
conta.sacar(30)
conta.sacar(1000)
conta.depositar(-10)
conta.mostrar_saldo()


        


        
        
