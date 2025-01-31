class Produto:
    def __init__(self,nome,preco,quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def PrecoTotal(self) -> float:
        return self.__preco * self.__quantidade
    def QuantidadeEmEstoque(self) -> float:
        return self.__quantidade
    


nome = input("Qual o nome do produto? ")
preco = float(input("Qual o preco do produto? "))
quantidade = int(input("Digite a quantidade: "))



newProduct = Produto()



while True:
    opcao = int(input("Digite o que você quer fazer: \n1.Visualizar preço total\n2.Verifica Quantidade em Estoque"))
    match opcao:
        case 1: 
            newProduct.PrecoTotal()
        case 2:
            newProduct.QuantidadeEmEstoque()