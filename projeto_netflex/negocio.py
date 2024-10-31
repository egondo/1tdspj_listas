import banco
from datetime import datetime

def insere_midia(filme: dict):
    #regra de negocio: não posso incluir midias com o mesmo titulo
    dados = banco.recupera_midia_titulo(filme['titulo'])
    if dados:
        #gerar uma excecao desta funcao
        raise Exception("Midia ja existente")
    else:
        banco.insere_midia(filme)

def converte_midia_dict(midia: tuple) -> dict:
    return {"id": midia[0], "titulo": midia[1], "categoria": midia[2], "tipo": midia[3], "nota": midia[4]*(1.0)/midia[5]}

def consulta_midias(id: int, titulo: str, categoria: str):
    if id:
        dado = banco.recupera_midia(id)
        if dado:
            return converte_midia_dict(dado)
    elif titulo:
        dados = banco.recupera_midia_titulo(titulo)
        resposta = []
        for reg in dados:
            resposta.append(converte_midia_dict(reg))
        return resposta
    elif categoria:
        dados = banco.recupera_midia_categoria(categoria)
        resposta = []
        for reg in dados:
            resposta.append(converte_midia_dict(reg))
        return resposta               
    

def assistir(id_usuario: int, id_midia: int, tipo: int):
    pref = {"id_usuario": id_usuario, "id_midia": id_midia, "acao": tipo, "datahora": datetime.now()}
    banco.insere_preferencia(pref)
    

if __name__ == "__main__":
    dado = consulta_midias(1, None, None)
    print(dado)   

    dado = consulta_midias(None, 'a', None)
    print(dado)   
    
    dado = consulta_midias(None, None, 'drama')
    print(dado)   
    