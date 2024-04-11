num = int(input("Número decimal: "))

soma = 0
pot10 = 1

while num != 0:
    resto = num % 2
    #print(resto)
    num = num // 2
    soma = soma + resto * pot10
    pot10 = pot10 * 10

print(f"Decimal {soma}")