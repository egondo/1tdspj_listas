def cadastra(servidor: dict):
    login = input("Informe o seu login: ")
    if login in servidor:
        print("ERRO, este login já existe!")
    else:
        servidor[login] = ["Bem vindo ao 1tdspj"]

def leitura(servidor: dict):
    login = input("Ler as mensagens de: ")
    if not login in servidor:
        print("Usuário não encontrado!") 
    else:
        mensagens = servidor[login]
        for msg in mensagens:
            print(msg)

def envio(servidor: dict):
    remetente = input("Para quem deseja enviar o email: ")
    if not remetente in servidor:
        print("Email não encontrado")
    else:
        lista_msgs = servidor[remetente]
        assunto = input("Assunto: ")
        lista_msgs.append(assunto)

usuarios = {}
opcao = 0
while opcao != 4:
    print("1 - cadastra usuario")
    print("2 - ler as mensagens")
    print("3 - enviar mensagem")
    print("4 - sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        cadastra(usuarios)
    elif opcao == 2:
        leitura(usuarios)
    elif opcao == 3:
        envio(usuarios)