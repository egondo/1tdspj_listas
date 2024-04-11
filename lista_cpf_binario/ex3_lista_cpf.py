cpf = int(input("Informe cpf 9: "))
while cpf > 999_999_999:
    cpf = int(input("Inválido, digite novamente: "))

cpf_bak = cpf

soma = 0
mult = 2
while cpf != 0:
    dig = cpf % 10
    soma = soma + dig * mult
    cpf = cpf // 10
    mult = mult + 1

resto = soma % 11
if resto < 2:
    print("primeiro digito: 0")
    cpf = cpf_bak * 10
else:
    print(f"primeiro dígito: {11-resto}")
    cpf = cpf_bak * 10 + (11 - resto)
