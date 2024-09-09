input_correto = False

while not input_correto:
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        salario = float(input("Salario: "))
        input_correto = True
    except:
        print("Erro na entrada de dados!")
