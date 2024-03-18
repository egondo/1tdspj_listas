import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

if a == 0:
    print("Esta não é uma equação de 2 grau!")

else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print(f"Não existem raízes reais para esta equação: {delta} é menor que 0")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes são: {x1} e {x2}")