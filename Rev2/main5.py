class Funcionario:
    def __init__(self,nome :float ,salario : float ,cargo:str):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo


    def DescontoSetter(self, lista) -> None:
        self.__desconto : float = sum(lista)

    def CalculaDesconto(self) -> None:
        self.__salario -= self.__desconto
        
    def DescontoGetter(self) -> float:
        return self.__desconto

    def SalarioGetter(self) -> float:
        return self.__salario
    

novoFuncionario = Funcionario()


while True:
    opcao = int(input("Digite uma opcao: \n1.Calcula Desconto\n2.Insere os valores de desconto\n3.Vê os valores de desconto\n4.Vê o valor do salário\n5.Sair"))
    match opcao:
        case 1:
            novoFuncionario.CalculaDesconto()
            print("Realizado!")
        case 2: 
            x = input("Digite os valores separados por , :").split(",")
            listaFloat = [float(i) for i in x]
            novoFuncionario.DescontoSetter(listaFloat)
        case 3:
            print(novoFuncionario.DescontoGetter)
        case 4:
            print(novoFuncionario.SalarioGetter)
        case 5: 
            exit()

    