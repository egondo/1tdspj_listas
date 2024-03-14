rm = int(input("Digite RM com 5 ou menos digitos: "))

soma = 0

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

print(f"O resultado vale {soma}")




