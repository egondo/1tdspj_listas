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
