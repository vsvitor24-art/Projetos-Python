class Personagem:
    def __init__(self, nome, vida, vida_maxima, ataque, defesa):
        validações= {
            "nome": str, 
            "vida_maxima" : int,
            "vida": int,
            "ataque" : int,
            "defesa": int
        }

        for itens in validações:
            valor_real = locals()[itens]
            tipo_esperado = validações[itens]
            
            if not isinstance(valor_real, tipo_esperado):
                raise TypeError("Error: TypeError")
            return

        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida_maxima
        self.ataque = ataque
        self.defesa = defesa


    def atacar(self,alvo):



    def receber_dano(dano):

    def esta_vivo():

        
#Métodos: atacar(alvo), receber_dano(dano), esta_vivo(), __str__()