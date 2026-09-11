def validar_hp(hp):
    if hp <0:
        raise ValueError("hp nao pode ser negativo")
    print("hp valido")

validar_hp(10)   
validar_hp(0)     
validar_hp(-5)  

