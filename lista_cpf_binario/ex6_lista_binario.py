#converte um número decimal para hexadecimal

num = int(input("Informe o número: "))
resp = ""
while num != 0:
    resto = num % 16
    num = num // 16
    if resto < 10:
        resp = str(resto) + resp
    elif resto == 10:
        resp = 'A' + resp
    elif resto == 11:
        resp = 'B' + resp
    elif resto == 12:
        resp = 'C' + resp
    elif resto == 13:
        resp = 'D' + resp
    elif resto == 14:
        resp = 'E' + resp
    else:
        resp = 'F' + resp

print(resp)