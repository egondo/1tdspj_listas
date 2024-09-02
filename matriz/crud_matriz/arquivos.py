def grava_arquivo(matriz: list, nome: str):
    arq = open(nome, mode="w")
    for linha in matriz:
        for dado in linha:
            arq.write(str(dado))
            arq.write(";")
        arq.write("\n")
    arq.close()

def le_arquivo(nome: str) -> list:
    retorno = []
    arq = open(nome, mode="r")
    for linha in arq:
        #print(linha)
        dados = linha.split(";")
        reg = []
        for i in range(6):
            if i < 5:
                reg.append(dados[i])
            else:
                reg.append(float(dados[i]))
                
        retorno.append(reg)
    return retorno