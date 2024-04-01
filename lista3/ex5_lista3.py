n = int(input("Informe  um número inteiro positivo: "))

#faça a validação de n, ou seja, não permita n < 0

divisor = 1
contagem_divisor = 0

while divisor <= n:
    if n % divisor == 0:
        contagem_divisor = contagem_divisor + 1
    divisor = divisor + 1

print(f"{n} possui {contagem_divisor} divisores")    