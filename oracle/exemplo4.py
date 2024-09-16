import oracledb

url = "oracle.fiap.com.br/orcl"
con = oracledb.connect(user='pf0313', dsn=url, password='professor#23')

cur = con.cursor()
sql_ins = '''delete from empregado where numero= :numero'''
dado = {"numero": 87}

cur.execute(sql_ins, dado)
con.commit()
cur.close()
con.close()