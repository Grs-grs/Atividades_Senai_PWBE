def inverte_string(x : str):
    string_fatiada = list(x)
    tamanho = len(string_fatiada) - 1
    string_nova_fatiada = [] 
    while (tamanho >= 0):
        string_nova_fatiada.append(string_fatiada[tamanho])
        tamanho -= 1
    string_fatiada = string_nova_fatiada.split(",")
    return string_fatiada