num = float(input("Digite o numero: "))

raiz = 0
delta = 0.000001

while raiz * raiz < num:
    raiz = raiz + delta

raiz = raiz - delta
print(f"A raiz de {num} é {raiz}")    