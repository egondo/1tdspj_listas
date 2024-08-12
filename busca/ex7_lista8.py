def busca_todos(lista: list, valor: object) -> list:
    resp = []
    for i in range(len(lista)):
        if lista[i] == valor:
            resp.append(i)
    return resp

if __name__ == '__main__':
    lst = [2, 9, -5, 8, 8, 4, 2, 5, 4, 7, 3, 7]
    resp = busca_todos(lst, 1)
    print(resp)

            