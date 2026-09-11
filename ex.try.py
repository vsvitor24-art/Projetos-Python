def dividir_seguro(a, b):
    if b == 0:
        print("Erro: divisão por zero não é permitida")
        return
    
    try:
        resultado = a / b
        print(resultado)
    except TypeError:
        print("Erro: forneça apenas números")


# Aqui embaixo é onde a gente USA a função, fora dela
print("Testando com 10 e 2:")
dividir_seguro(10, 2)

print("Testando com 10 e 0:")
dividir_seguro(10, 0)

print("Testando com 10 e 'abc':")
dividir_seguro(10, "abc")

print("Tentativa de divisão finalizada.")

