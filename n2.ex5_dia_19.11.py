def media_centralizada(numeros):
    if len(numeros) <= 2:
        return 0
    maior = max(numeros)
    menor = min(numeros)
    numeros_filtrados = numeros.copy()
    numeros_filtrados.remove(maior)
    numeros_filtrados.remove(menor)
    return sum(numeros_filtrados) / len(numeros_filtrados)
