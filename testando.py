print("Cadastro de cliente".center(50))

#aqui eu vou criar uma função!
def dados(nome, idade, peso, altura):
    return nome, idade, peso, altura
while True:
    try:
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        break
    except :
        print("Algum campo esta incorreto, preencha os campos corretamente!")
    
while nome =="" or idade=="" or idade<=0 or peso<=0 or altura<=0:
    print("Algum campo esta incorreto, preencha os campos corretamente!")
    nome=input("Digite seu nome: ")
    idade=int(input("Digite sua idade: "))
    peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: "))

print(f"Olá {nome}, voce tem: {idade} anos, pesa:{peso} kgs e tem {altura} metros de altura")

if idade >=60:
    print("voce é um idoso")
elif idade >=18:
    print("voce é um adulto jovem")
elif idade <=17:
    print("voce é uma criança")

cadastro = dados(nome, idade, peso, altura)

while True:
    try:
        acesso =int(input("Digite a senha 123 para acessar tuas informaçoes: "))
        if acesso == 123:
            print(f"Aqui estao suas informaçoes, {nome}: ")
            print(f"{cadastro}")
            break
        else:
            print("Senha incorreta, tente novamente!")
    except: 
        print("Digite apenas numeros, tente novamente!")


