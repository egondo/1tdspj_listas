import oracledb

url = "oracle.fiap.com.br/orcl"
conn = oracledb.connect(user='pf0313', password='professor#23', dsn=url)
print("Versao do banco " + conn.version)

cursor = conn.cursor()
cursor.execute('SELECT * FROM PACIENTE')
reg = cursor.fetchall()
print("Tipo de objeto retornado: ", type(reg))

for info in reg:
    print(info)

cursor.close()
conn.close()