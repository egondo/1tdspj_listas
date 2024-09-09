def busca(matriz: list, valor: object) -> list:
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == valor:
                return [i, j]
    
    return [-1, -1]

#faça o teste aqui da busca