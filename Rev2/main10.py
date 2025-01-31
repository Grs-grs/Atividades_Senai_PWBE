class Livro:

    def __init__(self,titulo,autor,paginas):
        self.__titulo = " "
        self.__autor = " "
        self.__paginas = 0
        self.__disponivel = True

    def  EmprestarLivro(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Livro foi emprestado")
        else: 
            print("Livro não disponível")

    def DevolverLivro(self):
        if(not(self.__disponivel)):
            print("Livro devolvido")
            self.__disponivel - True
        else:
            print("Please. Try again later...")

    def Verificar(self) -> float:
        return self.__disponivel
    
titulo,autor = map(strig, input("Digite os nomes do titulo e autor respectivamente: "))
paginas = int(input("Digite a quantidade de páginas: "))
novoLivro = (titulo,autor,paginas)
