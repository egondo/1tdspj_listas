'''Inserindo um registro em tb_enquete com 
auto increment no id e recuperando o valor inserido'''

import oracledb

url = "oracle.fiap.com.br/orcl"
con = oracledb.connect(user='pf0313', dsn=url, password='professor#23')

cur = con.cursor()
sql_ins = '''insert into tb_enquete(nome, descricao, criador, datacriacao)
            values(:nome, :descricao, :criador, to_date(:data,'YYYY-MM-DD'))
            returning id into :id'''

new_id = cur.var(oracledb.NUMBER)
dado = {"nome": "Checkpoint 5", "descricao": "Oracle", 'criador': 'Eduardo', 
        'data': '2024-09-23', 'id': new_id}

cur.execute(sql_ins, dado)

print(dado)
con.commit()
cur.close()
con.close()