def menu():
    print("1 - Insere livro")
    print("2 - Lista livro")
    print("3 - Sair")
    opcao = int(input("Escolha uma opcao: "))
    return opcao

def insere_livro(lista):
    print("\nInserindo livro:\n")
    tit = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano lançamento: "))
    preco = float(input("Preço: "))
    lista.append(tit)
    lista.append(autor)
    lista.append(ano)
    lista.append(preco)

def lista_livros(lista):
    i = 0
    while i < len(lista):
        print(f"{i}: {lista[i]} - {lista[i+1]}")
        i = i + 4
    opcao = int(input("Posição do livro ou -1 para nenhum: "))
    return opcao


def submenu():
    print("1 - altera\n2 - exclui")
    return int(input("Selecione: "))

def altera_exclui(lista, pos, opcao):
    if opcao == 2: #exclui
        for i in range(4):
            lista.pop(pos)
    elif opcao == 1: #altera
        tit = input(f"Título ({lista[pos]}): ")
        if len(tit) > 0:
            lista[pos] = tit
        
        aut = input(f"Autor ({lista[pos+1]}): ")
        if len(aut) > 0:
            lista[pos + 1] = aut
        
        ano = input(f"Ano ({lista[pos+2]}): ")
        if len(ano) > 0:
            lista[pos + 2] = int(ano)
        
        prc = input(f"Preço ({lista[pos+3]}): ")
        if len(prc) > 0:
            lista[pos + 3] = float(prc)






op = menu()
livros = [] 
livros = ['Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997, 50.89, 'O Menino do Engenho', 'Zé Lins do Rego', 1932, 35.5]

while op != 3:
    if op == 1:
        insere_livro(livros)
        print(livros)
    elif op == 2:
        pos = lista_livros(livros)
        print(f"Selecionado livro: {livros[pos]}")
        acao = submenu()
        altera_exclui(livros, pos, acao)

    op = menu()


