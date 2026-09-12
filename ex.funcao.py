def calcular_dano(ataque, hp):

    try:
        if not isinstance(ataque, int):
            raise TypeError("numeros invalidos")
        elif not isinstance(hp, int):
            raise TypeError("numeros invalidos")

        resultado = ataque - hp

        if ataque > hp:
            print(f"Inimigo eliminado, {resultado}")
        else:
            print(f"Dano causado: {resultado}")

        return resultado
    
    except TypeError:
        print("Erro: entrada invalida, numeros esperados")
        raise



calcular_dano(40, 10)

calcular_dano(40, 100)

calcular_dano(10, -5 )

calcular_dano(10, "abc")

calcular_dano("abc", 60)

