mat = []
for i in range(4):
    mat.append([0] * 5)

num = 1
for lin in range(4):
    for col in range(5):
        mat[lin][col] = num
        num = num + 1

for linha in mat:
    print(linha)