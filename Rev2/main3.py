import Figura



class Retangulo(Figura):

    def __init__(self, base,altura,lado1,lado2,lado3):
        self.__base = base
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2 
        self.__lado3 = lado3

    def Area(base,altura):
        return ((base*altura) / 2)
    
    def Perimetro(lado1,lado2,lado3):
        return lado1+lado2+lado3
    

    
Rect = Retangulo()

opcao = int(input("Digite uma opcao: \n1.Calcular area\n2.Calcular perimetro"))


match opcao:
    case 1:
        b = int(input("Digite a base: "))
        h = int(input("Digite a altura: "))
        print(Rect.Area())
    case 2:
        lado1 = int(input("Digite o primeiro lado: "))
        lado2 = int(input("Digite o segundo lado: "))
        lado3 = int(input("Digite o terceiro lado: "))
        print(Rect.Perimetro())



