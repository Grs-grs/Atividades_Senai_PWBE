def contaString(string : str):
    dicionario = {}
    for i in string:
        dicionario[i] = dicionario.get(i,0) + 1
    return dicionario
