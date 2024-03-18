import math

numero = float(input("Informe um número não negativo: "))

raiz_2 = numero ** 0.5

print(raiz_2)

if numero < 0:
    print("Impossível extrair a raiz quadrada!")
else:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz}")
