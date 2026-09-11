def calcular_media_segura(nota1, nota2):
    
    try:
        if nota1 < 0 or nota2 <0:
                print("Erro: notas não podem ser negativas")
                return
        
        resultado = (nota1 + nota2) / 2
        print(resultado)
    
    except TypeError:
        print("Erro: forneça apenas números")


calcular_media_segura(8, 6)
calcular_media_segura(-5, 7)
calcular_media_segura(8, "dez")

print("Cálculo de média finalizado.")




