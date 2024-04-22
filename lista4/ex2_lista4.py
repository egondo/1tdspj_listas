palavra = input("Informe a palavra: ")

resp = ""
i = 0
while i < len(palavra):
    resp = resp + palavra[i] + " "
    i = i + 1

print(resp)
