class Agenda:
    contatos = {}
    
    def AdicionarContato():
        nome = input("Digite o nome do contato: ")
        numero = int(input("Digite o número: "))
        Agenda.contatos[nome] = numero

    def RemoverContato():
        nome = print("Digite o nome do contato que deseja excluir: ")
        del Agenda.contatos[nome]
    
    def EditarNumero():
        nome = input("Digite o nome do contato para substituir o numero: ")
        numero = int(input("Digite o número para substituir o outro: "))
        Agenda.contatos[nome] = numero

    def BuscarContatos():
        escolha = int(input("1.Procurar por número\n2.Procurar pelo nome"))
        match escolha:
            case 1:
                nome = input("Digite o nome do contato: ")
                resultado = Agenda.contatos[nome] 
                print(f"Resultado:{resultado}")
            case 2: 
                numero = int(input("Digite o numero: "))
                resultado = [nome for nome,num in Agenda.contatos.items if num == numero]
                print(f"Nome: {resultado}")

controler = Agenda()

while True:
    escolha = int(input("1.Adicionar Contato\n2.Remover Contato\n3.Editar Contato\n4.Buscar Contato"))
    match escolha:
        case 1:
            controler.AdicionarContato()
        case 2:
            controler.RemoverContato()
        case 3:
            controler.EditarNumero()
        case 4:
            controler.BuscarContatos()
        
