lista_numeros:int = [] 

i : int = 0

while True:
    i = int(input("Digite um número"))
    if i >= 0:
        lista_numeros.append(i)
    else:
        break


maior = max(lista_numeros)

print(maior)