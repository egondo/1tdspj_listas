import time

def busca(conjunto: list, valor: float) -> int:
    i = 0
    while i < len(conjunto) and conjunto[i] != valor:
        i = i + 1

    if i == len(conjunto):
        return -1
    else:
        return i
    

lista = [-5.6, 0.9, 3.6, 2.0, -1.8, 4.2, 3.7, -7.1, 10]
x = 3.2
resp = busca(lista, x)
print(resp) 

lista = [0] * 100_000_000
x = -10
for i in range(len(lista)):
    lista[i] = i

t_ini = time.time()
resp = busca(lista, x)
t_fim = time.time()
print(t_fim - t_ini)
print(resp)
