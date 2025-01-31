import random

class ContaBancaria:
    def __init__(self, nome):
        self.__numero_conta = random.randint(0, 9999999)
        self.__saldo : float = 0
        self.__nome : str = nome

    def saldoSetter(self, tipo : bool, amount : float):
        if tipo == True:
            self.__saldo += amount
        else:
            self.__saldo -= amount
    def saldoGetter(self):
        return self.__saldo
    
sistema = ContaBancaria()


while True:
    x = input('''
    Bem-vindo ao banco ResendePay\n1.Sacar\n2.Depositar\n3.Ver saldo\n4.Sair
    ''')
    if x == 1:
        tipo = False
        saldo = float(input("Digite o saldo a sacar"))
        sistema.saldoSetter(tipo=tipo, amount=saldo)
    elif x == 2 :
        tipo = True
        saldo = float(input("Digite o saldo a depositar"))
        sistema.saldoSetter(tipo=tipo, amount=saldo)
    elif x == 3:
        print(sistema.saldoGetter())
    elif x == 4:
        exit()