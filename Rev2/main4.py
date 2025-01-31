class Aluno:
    def __init__(self,nome,matricula,notas):
        self.__nome : str
        self.__matricula : str
        self.__notas : list = []
        self.__situacao : bool 
    
    def CalculaNota(self) -> float:
        soma = sum(self.__notas)
        media = soma / (len(self.__notas)) 
        return media 
    
    def NotasGetter(self) -> list:
        return self.__notas
    
    def Situacao(self):
        notaFinal= self.CalculaNota()
        soma = sum(self.__notas)
        if soma >= notaFinal:
            self.__situacao = True
        elif soma < notaFinal:
            self.__situacao = False
    
    def AdicionaNota(self, lista : list) -> None:
        novasNotas = [float(i) for i in lista]
        self.__notas += novasNotas



aluno = input("Digite o nome do aluno: ")
matricula = input("Digite o número de matricula do aluno: ")
notas = input("Digite as notas:").split(",")


newAluno = Aluno(aluno=aluno, matricula=matricula,notas=notas)

while True:
    opcao = int(input("Digite a opcao desejada:\n1. Calcular média\n2.Ver as notas atuais.\n3.Adicionar mais notas\n4.Verificar situação\n5.Sair"))

    match opcao:
        case 1:
            print(newAluno.CalculaNota())
        case 2:
            print(newAluno.NotasGetter)
        case 3:
            novasNotas = input("Digite as notas:").split(",")
            newAluno.AdicionaNota(novasNotas)
        case 4:
            newAluno.Situacao()
        case 5:
            exit()

    