#iniciamos com a entrada de dados

num = int(input("Digite um nº entre 0 e 99: "))

unidade = num % 10
dezena = num // 10

print("Unidade:", unidade, "dezena:", dezena)