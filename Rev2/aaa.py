class Agenda:
    contatos = {
        "João": "123456789",
        "Maria": "987654321",
        "Pedro": "456123789"
    }

def BuscarContatos():
    escolha = int(input("1. Procurar por nome\n2. Procurar por número\n"))

    match escolha:
        case 1:
            nome = input("Digite o nome do contato: ")
            if nome in Agenda.contatos:
                resultado = Agenda.contatos[nome]
                print(f"Resultado: {resultado}")
            else:
                print("Contato não encontrado.")
        case 2:
            numero = input("Digite o número: ")
            resultado = [nome for nome, num in Agenda.contatos.items() if num == numero]
            if resultado:
                print(f"Resultado: {resultado}")
            else:
                print("Número não encontrado.")
        case _:
            print("Opção inválida.")

# Exemplo de uso
BuscarContatos()
