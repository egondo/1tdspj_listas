def imprime(matriz):
    for linha in matriz:
        print(linha)

tabuleiro = []
for i in range(3):
    tabuleiro.append([''] * 3)

imprime(tabuleiro)
input()
tabuleiro[0][0] = 'X'
tabuleiro[1][1] = 'O'
tabuleiro[2][2] = 'X'

imprime(tabuleiro)