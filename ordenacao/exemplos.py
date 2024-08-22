def esta_ordenada(lista: list) -> bool:
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            return False
        i = i + 1

    return True

l = [2, 5, 8, 9, 10, 11]
resp = esta_ordenada(l)
print(resp)

k = [9, 7, 4, 9, 10, 11]
resp = esta_ordenada(k)
print(resp)