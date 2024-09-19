arq = open("municipio.txt")

for registro in arq:
    #print(registro)
    campos = registro.split(";")
    cod_uf = int(campos[1])
    uf = campos[0]
    cod_mun = int(campos[2])
    mun = campos[3]

    print(f"insert into estado(id, uf) values({cod_uf}, '{uf}');")
    print(f"insert into municipio values({cod_mun}, '{mun}', {cod_uf});")