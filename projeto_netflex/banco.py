import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_midia(midia: dict):
    sql = "insert into tbj_midia(titulo, categoria, tipo) values(:titulo, :categoria, :tipo)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, midia)

def recupera_midia(id: int):
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes, tipo from tbj_midia where id = :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
            return cur.fetchone()                            
            