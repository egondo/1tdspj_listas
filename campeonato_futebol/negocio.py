import banco

def cadastra_time(nome: str) -> dict:
    time = banco.consulta_time(nome)
    if time == None:
        time = {'nome': nome, 'vitorias': 0, 'empates': 0,
                'derrotas': 0, 'gols_pro': 0, 'gols_contra': 0}
        banco.insere_time(time)
    return time


def cadastra_partida(partida: dict):
    #para cada time dentro da partida, 
    #faço a consulta dele no banco
    #Se ele não existe, preciso cadastrá-lo no banco
    #verifico o vencedor da partida e atualizo as 
    #informações de acordo com o resultado
    #atualizo os time no banco de dados
    time_casa = cadastra_time(partida['casa'])
    time_visi = cadastra_time(partida['visi'])

    print("PARTIDA ", partida)

    if partida['gc'] > partida['gv']:
        time_casa['vitorias'] = time_casa['vitorias'] + 1
        time_visi['derrotas'] = time_visi['derrotas'] + 1
    elif partida['gc'] < partida['gv']:
        time_casa['derrotas'] = time_casa['derrotas'] + 1
        time_visi['vitorias'] = time_visi['vitorias'] + 1
    else:
        time_casa['empates'] = time_casa['empates'] + 1
        time_visi['empates'] = time_visi['empates'] + 1
            
    time_casa['gols_pro'] = time_casa['gols_pro'] + partida['gc']
    time_casa['gols_contra'] = time_casa['gols_contra'] + partida['gv']

    time_visi['gols_pro'] = time_visi['gols_pro'] + partida['gv']
    time_visi['gols_contra'] = time_visi['gols_contra'] + partida['gc']

    banco.atualiza_time(time_casa)
    banco.atualiza_time(time_visi)

    partida['casa'] = time_casa['id']
    partida['visi'] = time_visi['id']

    banco.insere_partida(partida)


def consulta_tabela_classificao() -> list:
    times = banco.recupera_times()
    #calcular as informações faltantes da tabela: saldo gols, 
    #pontos, jogos e aproveitamento e mostrar e retornar 
    #todas as informações em uma lista de dicionarios
    retorno = []
    for reg in times:
        jogos = reg[2] + reg[3] + reg[4]
        pontos = reg[2] * 3 + reg[3]
        aprov = (pontos * 100) / (jogos * 3)

        dado = {"nome": reg[1], "vitorias": reg[2], "empates": reg[3], 
        "derrotas": reg[4], "gp": reg[5], "gc": reg[6], "jogos": jogos,
        "pontos": pontos, "aproveitamento": int(aprov)}
        
        retorno.append(dado)
    return retorno
    
