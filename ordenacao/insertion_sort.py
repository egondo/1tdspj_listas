def insere_ordenado(lista: list):
    pos = len(lista) - 1
    x = lista[pos]
    while pos > 0 and x < lista[pos-1]:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    lista[pos] = x

conjunto = [2, 5, 6, 10, 14, 23]
print(conjunto)
insere_ordenado(conjunto)
print(conjunto)