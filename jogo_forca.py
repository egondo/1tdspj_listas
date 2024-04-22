sorteada = "frango assado"
erros = 0

segredo = ""

for c in sorteada:
    if c == ' ':
        segredo = segredo + "   "
    else:
        segredo = segredo + "_ "

print(f"{segredo}\nerros: {erros}")
letra = input("Informe a letra: ").lower()

#pegue a letra digitada e gere o novo segredo
#suponha que a letra informada seja o a
#segredo -> _ _ a _ _    a _ _ a _ _

segredo = ""
for c in sorteada:
    if c == ' ':
        segredo = segredo + "   "
    elif c == letra:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "

print(f"{segredo}\nerros: {erros}")