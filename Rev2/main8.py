class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.__marca : str = marca
        self.__modelo: str = modelo
        self.__velocidade : float = velocidade

    def Acelerar():
        print("Vruum...")
    def Freiar():
        print("SkrrSkrrSkrrSkrr...")
    def VelocidadeAtual(self):
        return self.__velocidade
    

modelo = input("Digite o modelo do carro: ")
marca = input("Digite a marca do carro")
velocidade = float(input("Digite a velocidade do carro: "))

Carrao = Carro(marca=marca, modelo=modelo, velocidade=velocidade)

while True:
    opcao = int(input("1.Acelerar\n2.Freiar\n3.Verificar velocidade\n4.Pular do carro"))
    match(opcao):
        case 1:
            Carrao.Acelerar()
        case 2:
            Carrao.Freiar()
        case 3: 
            Carrao.VelocidadeAtual
        case 4:
            print("seu maluco...")
            exit()
            