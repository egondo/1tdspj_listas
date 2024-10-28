from flask import Flask, request, jsonify
import negocio


app = Flask(__name__)

@app.route("/midias", methods=["POST"])
def insere_filme():
    dado = request.json
    try:
        negocio.insere_midia(dado)
        return {"midia": dado, "status": 201}, 201
    except:
        return {'title': 'Filme nao cadastrado', "status": 403}, 403
    

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
        return {'title': "erro inesperado", "status": 404}, 404


app.run(debug=True)
 # type: ignore