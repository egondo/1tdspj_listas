def descer(vetor: list):
    pos = 0
    while pos < len(vetor) - 1:
        if vetor[pos] > vetor[pos+1]:
            aux = vetor[pos+1]
            vetor[pos+1] = vetor[pos]
            vetor[pos] = aux
        pos = pos + 1


def bubble_sort(vetor: list):
    for i in range(len(vetor)):
        descer(vetor)

lista = [2, 10, 7, 12, 4, 6, 3, 10, 8]
bubble_sort(lista)
print(lista)