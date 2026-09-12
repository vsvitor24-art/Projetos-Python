class Mago:
    def __init__(self, mana, nivel):
        if not isinstance(mana, int):
            raise TypeError("Erro: TypeError")
        elif not isinstance(nivel, int):
            raise TypeError("Erro: TypeError")
        self.mana = mana
        self.nivel = nivel

        
    def lançar_feitiço(self, dano):
        if not isinstance(dano, int):
            raise TypeError("Erro: TypeError")
        
        if self.mana > dano:
            self.mana -= dano
            print(f"feitiço lançado, Dano causado: {dano},  Mana restante: {self.mana}")
        
        else:
            print("Não é possivel lançar o feitiço")

    
        


Mago1 = Mago(100, 60)

Mago2 = Mago(30,15)

Mago1.lançar_feitiço(40)

Mago2.lançar_feitiço(50)








