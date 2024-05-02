def aumento(valor, percentual):
    valor = valor + valor * percentual / 100
    return valor


def divisao_resto(a, b):
    return (a // b, a % b)

vl = 1000
perc = 25
aux = aumento(vl, perc)
print(aux)
#note que vl nao sofre modificacao pq int é imutável no python
print(vl) 

aux = aumento(400_000, 0.5)
print(aux)

result = divisao_resto(34, 7)
print(result)