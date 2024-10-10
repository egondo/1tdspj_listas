from flask import Flask, request, jsonify
import negocio

app = Flask(__name__)

#apenas duas entradas na API:
# - cadastra partida
# - lista times

@app.route("/partidas", methods=["POST"])
def cria_partida():
    partida = request.json
    negocio.cadastra_partida(partida)
    return partida, 200


@app.route("/times", methods=["GET"])
def lista_times():
    return negocio.consulta_tabela_classificao()    







app.run(debug=True)