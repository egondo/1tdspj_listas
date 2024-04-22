palavra = input("Informe a palavra: ")

resp = ""
resp2 = ""

for letra in palavra:
    resp = resp + letra + " "
    resp2 = f"{resp2}{letra} "

print(resp)
print(resp2)




