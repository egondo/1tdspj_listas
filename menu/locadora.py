# funcionalidades do sistema:
# alugar veículo
# devolver veículo
# cadastrar cliente
# consultar veículo disponível
opcao = 0
while opcao != 5:
    print("Sistema de locação")
    print("1 - alugar veículo")
    print("2 - devolver veículo\n3 - cadastrar cliente")
    print("4 - consultar veículo disponível")
    print("5 - sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        nascimento = input("Nascimento: ")
        habilitacao = int(input("Habilitação: "))
        print("Cadastro efetuado com sucesso!")
    elif opcao == 4:
        tipo = input("Informe o tipo do carro (Hath, Sedã, SUV): ")
        print("Carros disponíveis:")
        print("Ônix 2022 Turbo - 180,00")
        print("Polo 2020 1.6 - 200,00")
        print("Mobi 2023 1.0 - 140,00")
    elif opcao == 5:
        print("Obrigado por usar nosso sistema!")
    else:
        print("Opção inválida!")




