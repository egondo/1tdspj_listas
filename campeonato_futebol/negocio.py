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
    banco.insere_partida(partida)




#partida dicionario
jogo = {'casa': 'Palmeiras', 'visi': 'Botafoto', 
        'gv': 2, 'gc': 3, 'rodada': 1}
