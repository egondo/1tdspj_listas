import Imagem

matriz = Imagem.getMatrizImagemCinza("wallpaper.png")

lin = len(matriz)
col = len(matriz[0])
#criar outra matriz
rot = []
for i in range(lin):
    rot.append([0] * col)

#movendo os pixels para a matriz rot
for i in range(lin):
    for j in range(col):
        rot[lin - 1 - i][col - 1 - j] = matriz[i][j]

Imagem.salvaImagemCinza("wallpaper180.png", rot)



