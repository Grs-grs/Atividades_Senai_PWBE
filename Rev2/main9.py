from Rev2.main5 import novoFuncionario


class Paciente:
    def __init__(self):
        self.__historico = []
        self.__name = " "
        self.__idade : int = 0
        self.__historico : list

    @property
    def nome(self):
        return self.__name

    @nome.setter
    def name(self,value):
        if not isinstance(value, str):
            raise ValueError("O valor precisa ser string")
        else:
            self.__name = value

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self,value) -> None:
        if not isinstance(value, int):
            raise ValueError("O valor precisa ser um inteiro ")
        else:
            self.__idade = value


    @property
    def historico(self):
        return self.__historico

    @historico.setter
    def historico(self,value) -> None:
        if not isinstance(value, str):
            raise ValueError("O valor precisa ser uma string")
        else:
            self.__historico.append(value)




novoPaciente = Paciente()

nome = input("Digite seu nome: ")
novoPaciente.name = nome
idade = int(input("Digite sua idade: "))
novoPaciente.idade = idade
while True:
    opcao = input("Digite a opcao desejada:\n1.Quer adicionar uma nova consulta?\n2.Quer visualizar o histórico de consulta?\n3.Encerra a sessão")
    match opcao:
        case 1:
            novoFuncionario.historico = input("Digite quando foi: ")
        case 2:
            print(novoFuncionario.historico)














