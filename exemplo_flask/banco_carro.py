import oracledb
import os

def get_conexao():
    user = os.getenv("USER_BD")
    pwd = os.getenv("PASSWD_BD")
    print(user, pwd)
    return oracledb.connect(user=user, password=pwd,
                            dsn="oracle.fiap.com.br/orcl")


def insere(carro: dict):
    sql = "insert into tb_carro(montadora, modelo, ano, placa) values(:montadora, :modelo, :ano, :placa) returning id into :id"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            carro['id'] = novo_id
            cur.execute(sql, carro)
            carro['id'] = novo_id.getvalue()[0]
        conn.commit()

def recupera_id(id: int):
    sql = "select id, modelo, montadora, placa, ano from tb_carro where id=:id"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"id": id})
            reg = cur.fetchone()
            if len(reg) > 0:
                return {"id": reg[0], "modelo": reg[1], "montadora": reg[2], "placa": reg[3], "ano": reg[4]}
            else:
                return None

def update(carro: dict):
    sql = "update tb_carro set modelo=:modelo, montadora=:montadora, placa=:placa, ano=:ano where id=:id"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, carro)
        conn.commit()








