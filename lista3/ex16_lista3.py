num = int(input("Informe o número a ser validado:"))

dc = num % 10
num = num // 10

#print(f"{num} - {dc}")
mult = 2
soma = 0

while num != 0:
    dig = num % 10
    prod = dig * mult
    if prod >= 10:
        soma = soma + prod // 10 + prod % 10
    else:
        soma = soma + prod

    if mult == 2:
        mult = 1
    else:
        mult = 2
    num = num // 10


resto = soma % 10
dc_calculado = 0
if resto > 0:
    dc_calculado = 10 - resto

if dc == dc_calculado:
    print("Número válido!")
else:
    print("Número inválido!")