from flask import Flask, request, jsonify
import negocio
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5000")

#pip install flask_cors

#apenas duas entradas na API:
# - cadastra partida
# - lista times

@app.route("/partidas", methods=["POST"])
@cross_origin()
def cria_partida():
    partida = request.json
    negocio.cadastra_partida(partida)
    return partida, 200


@app.route("/times", methods=["GET"])
@cross_origin()
def lista_times():
    return negocio.consulta_tabela_classificao()    







app.run(debug=True)