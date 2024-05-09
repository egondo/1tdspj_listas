notas = []
n = int(input("Qtd de notas: "))

for x in range(0, n):
    valor_nota = float(input("nota: "))
    notas.append(valor_nota)
    #print(notas)

soma = 0
i = 0 
while i < len(notas):
    soma = soma + notas[i]
    i = i + 1

media = soma / n
print(media)
abaixo = 0
igual = 0
acima = 0
for n in notas:
    if n > media:
        acima = acima + 1
    elif n < media:
        abaixo = abaixo + 1
    else:
        igual = igual + 1

print(f"+: {acima}, =: {igual}, -: {abaixo}")


