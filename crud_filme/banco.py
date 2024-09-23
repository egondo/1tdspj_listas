import oracledb

def get_conexao():
    url = "oracle.fiap.com.br/orcl"
    return oracledb.connect(user="pf0313", password="professor#23",
                          dsn=url)

def insere_filme(filme: dict):
    sql = '''insert into t_filme(titulo, diretor, duracao, avaliacao,
            sinopse, classificacao, genero, data_lancamento) 
            values(:titulo, :diretor, :duracao, :avaliacao,
            :sinopse, :classificacao, :genero, 
            to_date(:data_lancamento, 'DD-MM-YYYY'))'''
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, filme)
        con.commit()

def consulta_genero(genero: str) -> list:
    sql = "select * from t_filme where genero like :gen order by data_lancamento desc"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"gen": f"%{genero}%"})
            lista = cur.fetchall()
            return lista
        
def altera_filme(filme: dict):
    sql = '''update t_filme set titulo=:titulo, diretor=:diretor, sinopse=:sinopse, data_lancamento=:data_lancamento, genero=:genero,
    classificacao=:classificacao, avaliacao=:avaliacao, duracao=:duracao
    where id=:id'''

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, filme)
        con.commit()

def apaga_filme(id: int):
    sql = "delete from t_filme where id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
        con.commit()
    
