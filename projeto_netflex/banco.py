import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_midia(midia: dict):
    sql = "insert into tbj_midia(titulo, categoria, tipo) values(:titulo, :categoria, :tipo)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, midia)
        con.commit()


def recupera_midia(id: int):
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes from tbj_midia where id = :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
            return cur.fetchone()                            
            
def recupera_midia_titulo(titulo: str):
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes from tbj_midia where titulo like :titulo"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"titulo": f"%{titulo}%"})
            return cur.fetchall()

def recupera_midia_categoria(categoria: str):
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes from tbj_midia where categoria like :categoria"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"categoria": f"%{categoria}%"})
            return cur.fetchall()

def insere_preferencia(pref: dict):
    sql = "insert into tbj_preferencias(datahora, id_midia, id_usuario, acao) values(:datahora, :id_midia, :id_usuario, :acao)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, pref)
        con.commit()

def recupera_preferencia_midia_usuario(id_usu: int, id_mid: int):
    sql = "select id, datahora, id_midia, id_usuario, acao from tbj_preferencias where id_midia=:id_midia and id_usuario=:id_usuario"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id_midia": id_mid, "id_usuario": id_usu})
            return cur.fetchone()

def recupera_filmes_assistidos_usuario(id_usu: int):
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes from tbj_midia where id in (select id_midia from tbj_preferencias where id_usuario = :id_usuario and acoes in (1, 3)) order by titulo"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id_usuario": id_usu})
            return cur.fetchall()
        
def recupera_filmes_listados_usuario(id_usu: int):
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes from tbj_midia where id in (select id_midia from tbj_preferencias where id_usuario = :id_usuario and acoes in (2, 3)) order by titulo"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id_usuario": id_usu})
            return cur.fetchall()


def recupera_midias():
    sql = "select id, titulo, categoria, tipo, avaliacao, qtd_avaliacoes from tbj_midia"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

def recupera_usuario():
    sql = "select id, nome, email, senha from tbj_usuario"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
