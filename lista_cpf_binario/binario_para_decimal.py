bin = int(input("Informe o número na base binária: "))

pot2 = 1
acum = 0

while bin > 0:
    dig = bin % 10
    bin = bin // 10
    acum = acum + dig * pot2
    pot2 = pot2 * 2

print(f"Resultado: {acum}")
