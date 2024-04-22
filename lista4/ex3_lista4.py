frase = input("Digite uma frase: ")

letra = input("Digite uma letra: ").lower()
while len(letra) != 1:
    letra = input("Erro, digite uma letra: ").lower()

letraM = letra.upper()
resp = ""

for c in frase:
    if c == letra or c == letraM:
        resp = resp + "*"
    else:
        resp = resp + c

print(resp)