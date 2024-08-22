def subir(lista, pos):
    i = len(lista) -  1
    while i > pos:
        if lista[i] < lista[i-1]:
            #troca das posicoes
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        i = i - 1

def bubble_sort(lista):
    for i in range(len(lista)):
        subir(lista, i)


if __name__ == "__main__":
    lst = [3, 5, 8, 2, 8, 4, 1]
    bubble_sort(lst)
    print(lst)       

    nomes = ["Elza", "Felipe", "Maria", "Bruna", "Andre", "Tomas", "Diego", "Samanta", "Vinicius"]
    bubble_sort(nomes)
    print(nomes)