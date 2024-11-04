from flask import Flask, request, jsonify
import negocio
import traceback


app = Flask(__name__)

@app.route("/midias", methods=["POST"])
def insere_filme():
    dado = request.json
    try:
        negocio.insere_midia(dado)
        return {"midia": dado, "status": 201}, 201
    except Exception as e:
        print("ERRO", e)
        return {'title': str(e), "status": 403}, 403

@app.route("/midias/<int:id>", methods=["GET"])
def recupera_midia(id):
    try:
        info = negocio.consulta_midias(id, None, None)
        return jsonify(info), 200
    except:
        return {'title': "erro inesperado", "status": 404}, 404

@app.route("/midias/categoria/<categoria>", methods=["GET"])
def recupera_midia_categoria(categoria):
    try:
        return negocio.consulta_midias(None, None, categoria), 200
    except:
        return {'title': "erro inesperado", "status": 404}, 404

@app.route("/midias/titulo/<titulo>", methods=["GET"])
def recupera_midia_titulo(titulo):
    try:
        return negocio.consulta_midias(None, titulo, None), 200
    except:
        traceback.print_exc()
        return {'title': "erro inesperado", "status": 404}, 404

@app.route("/midias/preferencia", methods=["POST"])
def assistir_midia():
    dado = request.json
    print(dado)
    try:
        negocio.assistir(dado['id_usuario'], dado['id_midia'], dado['tipo'])
        return {'title': "Vinculo estabelecido com sucesso", "status": 201}, 201
    except:
        return {'title': "Nao foi possivel vincular usuario com midia", "status": 404}, 404

@app.route("/midias", methods=["GET"])
def recupera_todas_midias():
    return negocio.recupera_midias()

@app.route("/usuarios", methods=["GET"])
def recupera_todos_usuarios():
    return negocio.recupera_usuarios()







app.run(debug=True)
 # type: ignore