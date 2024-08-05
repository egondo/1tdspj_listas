import time

def busca_binaria(conjunto: list, valor: object) -> int:
    ini = 0
    fim = len(conjunto) - 1

    while ini <= fim:
        meio = (ini + fim) // 2
        if conjunto[meio] < valor:
            ini = meio + 1
        elif conjunto[meio] > valor:
            fim = meio - 1
        else:
            return meio
    
    return -1

lista = [0] * 100_000_000
x = -10
for i in range(len(lista)):
    lista[i] = i

t_ini = time.time()
resp = busca_binaria(lista, x)
t_fim = time.time()
print(t_fim - t_ini)


print(resp)
