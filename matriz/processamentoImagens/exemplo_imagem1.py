import Imagem

matriz = Imagem.getMatrizImagemCinza("floresta.jpg")

lin = len(matriz)
col = len(matriz[0])
print(f"Dimensoes {lin}X{col}")

for i in range(lin):
    for j in range(col):
        if matriz[i][j] <= 100:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 255

Imagem.salvaImagemCinza("floresta2.jpg", matriz)