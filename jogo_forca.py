sorteada = "frango assado"
erros = 0
chutadas = " "

segredo = ""
for c in sorteada:
    if c in chutadas:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "

while erros < 6 and "_" in segredo:
    print(f"{segredo}\nerros: {erros}")
    letra = input("Informe a letra: ").lower()
    chutadas = chutadas + letra

    segredo = ""
    for c in sorteada:
        if c in chutadas:
            segredo = segredo + c + " "
        else:
            segredo = segredo + "_ "

    if not letra in sorteada:
        erros = erros + 1
    
if erros == 6:
    print(f"Você foi enforcado e a palavra era {sorteada}")
else:
    print(f"Parabéns, você acertou {sorteada}")    



    