import Figura

class Triangulo(Figura):
    def __init__(self, lado1,lado2,lado3,area,base):
        self.__lado1 = lado1
        self.__lado2 = lado2 
        self.__lado3 = lado3
        self.__area = area
        self.__base = base

    def VerificarTriangulo(self):
        if self.__lado1 + self.__lado2 > self.__lado3 and self.__lado2 + self.__lado3 > self.__lado1 and self.__lado1+self.__lado3 > self.__lado2:
            return True
        else:
            return False
        
    def CalculaArea(self):
        return (self.__area * self.__base) / 2
    

Triangle = Triangulo()

x1,x2,x3 = map(float,(input("Digite os números separados por ',' ").split(",")))
b,h = map(float, input("Digite a base e altura respectivamente separados por ',' "))

while True: 
    x = int(input("Digite a opcao desejada: \n1.Verificar se o triangulo inserido é valido.\n2.Verificar a base"))
    match x:
        case 1:
            print(Triangle.CalculaArea())

        case 2: 
            if Triangle.VerificarTriangulo() == True:
                print("Sim, o triangulo é válido.")
            else:
                print("Não,o triangulo é inválido.")


