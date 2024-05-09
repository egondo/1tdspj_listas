import random

def maior_menor(lista):
    maximo = lista[0]
    minimo = lista[0]

    for dado in lista:
        if dado > maximo:
            maximo = dado
        if dado < minimo:
            minimo = dado
    return (minimo, maximo)

numeros = []
for x in range(7):
    numeros.append(random.randint(0, 20))
print(numeros)
resposta = maior_menor(numeros)
print(resposta)
