class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print("Livro emprestado")
        else:
            print ("Livro já está emprestado")

    def devolver(self):
        self.emprestado = False
    
    def status(self):
        if self.emprestado == True:
            return f"{self.titulo} - Emprestado"
        else:
            return f"{self.titulo} - Disponível"

livro1 = Livro("O Senhor dos Anéis", "Tolkien")

print(livro1.status())        

livro1.emprestar()            

print(livro1.status())        

livro1.emprestar()            

livro1.devolver()
print(livro1.status())