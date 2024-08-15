def organiza(lista: list, pos: int):
    #pos = len(lista) - 1
    aux = lista[pos]

    while pos > 0 and lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1

    lista[pos] = aux

def insertion_sort(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)

if __name__ == '__main__':
    conj = [2, 6, 10, -1, 0, 4, 24, 17, 14, 15, 8, 6]
    insertion_sort(conj)
    print(conj)    