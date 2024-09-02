def cadastra(conj: list):
    tit = input("Informe o título: ")
    cat = input("Informe a categoria: ")
    sin = input("Sinopse:")
    aut = input("Autor(es): ")
    edi = input("Editora: ")
    prc = float(input("Preço: "))
    livro = [tit, cat, sin, aut, edi, prc]
    conj.append(livro)

def consulta(conj: list):
    resultado = []
    cat = input("Informe a categoria: ")
    for i in range(len(conj)):
        if conj[i][1] == cat:
            resultado.append(conj[i])
    
    if len(resultado) == 0:
        print("Nenhum livro encontrado!")
    else:
        for livro in resultado:
            print(livro)

def busca(conj: list, titulo: str):
    for i in range(len(conj)):
        if conj[i][0] == titulo:
            return i
    return -1

def altera(conj: list):
    tit = input("Informe o título do livro que deseja alterar: ")
    pos = busca(conj, tit)
    if pos == -1:
        print("Não encontrei livros com este título!")
    else:
        rotulos = ["Título", "Categoria", "Sinopse", "Autor(es)", "Editora", "Preço"]
        for i in range(len(rotulos)):
            aux = input(f"{rotulos[i]} ({conj[pos][i]}): ")
            if len(aux) > 0:
                if rotulos[i] == "Preço":
                    conj[pos][i] = float(aux)
                else:
                    conj[pos][i] = aux
        
def exclui(conj: list):
    tit = input("Informe o título do livro que deseja excluir: ")
    pos = busca(conj, tit)
    if pos == -1:
        print("Não há livros com este título!")
    else:
        print(conj[pos])
        print("Livro excluído com sucesso!")
        conj.pop(pos)








estoque = []
#quais informações de livros vamos armazenar?
#titulo, categoria, sinopse, autor, editora, preço
opcao = 0
while opcao != 5:
    print("     SISTEMA DE LIVRARIA     ")
    print("1 - cadastra")
    print("2 - consulta")
    print("3 - altera")
    print("4 - exclui")
    print("5 - sair")
    try:
        opcao = int(input("Informe uma opção: "))
    except Exception:
        print("Opção inválida!")
        opcao = 0
    
    if opcao == 1:
        cadastra(estoque)
    elif opcao == 2:
        consulta(estoque)
    elif opcao == 3:
        altera(estoque)
    elif opcao == 4:
        exclui(estoque)
    