class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def adicionar_ponto(self, pontos):
        if pontos < 0:
            print("pontuação invalida")
        else:
            self.nota += pontos
            print(f"Adicionado {pontos} pontos. Nota atual: {self.nota}")

    def remover_ponto(self,pontos):
        if pontos > self.nota:
            print("Não é possível remover mais pontos que o aluno possui")
        elif pontos < 0:
            print("Pontuação invalida")
        else:
            self.nota -= pontos
            print(f"Removido {pontos} pontos. Nota atual: {self.nota}")

    def situacao(self):
        if self.nota >= 6:
            return "Aprovado" 
        else:
            return "Reprovado"

    def mostrar_info(self):
        print(f"Aluno: {self.nome} | Nota: {self.nota} | Situação: {self.situacao()}")

aluno = Aluno("João", 5)
aluno.mostrar_info()
aluno.adicionar_ponto(3)
aluno.mostrar_info()
aluno.remover_ponto(10)
aluno.adicionar_ponto(-2)
aluno.remover_ponto(2)
aluno.mostrar_info()

