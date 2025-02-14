class LojaVirtual:
    Produtos = {}
    Carrinho = {}

    def CadastrarProduto(nome : str, valor: float):
        if nome in LojaVirtual.Produtos:
            print("Erro produto já cadastrado")
        else:
            LojaVirtual.Produtos[nome] = valor
            print(f"Produto {nome} cadastrado")

    def GerarCarrinho():
        while True:
            escolha = int(input("Digite uma opcão a seguir:\n1.Adiciona produto ao carrinho\n2.Remove produto do carrinho\n3.Exibi o carrinho\n4.Calcula o total\n4.Sair"))
            match escolha:
                case 1:
                    produto = input("Digite o nome do produto: ")
                    if produto in LojaVirtual.Produtos:
                        quantidade = int(input("Digite a quantidade de produto que você deseja: "))
                        if produto in LojaVirtual.Carrinho:
                            LojaVirtual.Carrinho[produto] += quantidade
                        else:
                            LojaVirtual.Carrinho[produto] = quantidade
                    else:
                        print(f"Produto:{produto} não encontrado")
                case 2:
                    produto = input("Digite o nome do produto: ")
                    if produto in LojaVirtual.Carrinho:
                        quantidade = int(input("Digite a quantidade que deseja remover: "))
                        if quantidade >= LojaVirtual.Carrinho[produto]:
                            del LojaVirtual.Carrinho[produto]
                        else:
                            LojaVirtual.Carrinho[produto] -= quantidade
                    else: 
                        print("Produto não encontrado")
                case 3:
                    if not LojaVirtual.Carrinho:
                        print("Carrinho vazio.")
                    for produto,valor in LojaVirtual.Carrinho.items():
                        print(f"{produto}:R${valor}")
                case 4: 
                    LojaVirtual.calcularTotal()
                    break
                case 5: 
                    exit()

    def AplicarDesconto(total):
        desconto = 10/100
        novototal = total - (total*desconto)
        return novototal
    
    def calcularTotal():
        total = 0
        for produto, quantidade in LojaVirtual.Carrinho.items():
            total += quantidade * LojaVirtual.Produtos[produto]
        total_desconto = LojaVirtual.AplicarDesconto(total)
        print(f"Valor total é: {total_desconto}")
        pass

novocarrinho = LojaVirtual()
while True:
    escolha = print("1.Cadastrar produto\n2.Alterar o carrinho carrinho ou finalizar\n3.Sair")
    match escolha: 
        case 1:
            novocarrinho.CadastrarProduto()
        case 2:
            novocarrinho.GerarCarrinho()
        case 3:
             exit()