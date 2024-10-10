import oracledb

def get_conexao():
    return oracledb.connect(user='pf0313', password='professor#23',
                            dsn="oracle.fiap.com.br/orcl")


def recupera_times():
    sql = '''select id, nome, vitorias, empates, derrotas, 
        gols_pro, gols_contra from t_time'''
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            dado = cur.fetchall()
        return dado    


def consulta_time(nome: str) -> dict:
    sql = '''select id, nome, vitorias, empates, derrotas, 
        gols_pro, gols_contra from t_time where nome = :nome'''
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"nome": nome})
            dado = cur.fetchone()
        if not dado:
            return None
        else:
            return {'id': dado[0], 'nome': dado[1],
                    'vitorias': dado[2], 'empates': dado[3],
                    'derrotas': dado[4], 'gols_pro': dado[5],
                    'gols_contra': dado[6]}
            

def insere_time(time: dict):
    sql = '''insert into t_time(nome, vitorias, empates, derrotas,
        gols_pro, gols_contra) values(:nome, :vitorias, :empates,
        :derrotas, :gols_pro, :gols_contra) returning id into :id'''
    with get_conexao() as con:
        with con.cursor() as cur:
            new_id = cur.var(oracledb.NUMBER)
            time['id'] = new_id
            cur.execute(sql, time)
        con.commit()
        time['id'] = new_id.getvalue()[0]


def atualiza_time(time: dict):
    sql = '''update t_time set nome=:nome, vitorias=:vitorias, 
        empates=:empates, derrotas=:derrotas, gols_pro=:gols_pro,
        gols_contra=:gols_contra where id = :id'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, time)
        con.commit()

def insere_partida(partida: dict):
    sql = '''insert into t_partida(gols_casa, gols_visi, rodada,
            id_casa, id_visi) values(:gc, :gv, :rodada, :casa, 
            :visi)'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, partida)
        con.commit()