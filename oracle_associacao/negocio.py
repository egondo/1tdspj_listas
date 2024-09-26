import banco

def cadastra_venda(cliente: dict, venda: dict):
    cli = banco.recupera_cliente_documento(cliente['documento'])
    if not cli:
        banco.insere_cliente(cliente)
        venda['id_cliente'] = cliente['id']
    else:
        venda['id_cliente'] = cli[0]

    #print(venda)
    
if __name__ == "__main__":
    cli = {'nome': 'FIAP', 'email':'compras@fiap.br', 'documento': '23.784.903/0001-87'}
    ven = {'valor': 25_000, 'data': '26-10-2024'}
    cadastra_venda(cli, ven)
    print(cli)
    print(ven)