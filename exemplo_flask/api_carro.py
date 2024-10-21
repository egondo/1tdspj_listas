from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import db
import banco_carro as bc

app = Flask(__name__)

cors = CORS(app, origins="http://127.0.0.1:5000")
#CORS(app)

@app.route("/carros", methods=["GET"])
@cross_origin()
def get_all_carros():
    return  (jsonify(db.carros), 200)

@app.route("/carros/<int:id>", methods=["GET"])
@cross_origin()
def get_carro(id):    
    #return str(id), 200
    for car in db.carros:
        if car['id'] == id:
            return jsonify(car), 200
    
    return {'msg': 'Nenhum carro encontrado', 'status':404}, 404

@app.route("/carros", methods=['POST'])
@cross_origin()
def insere_carro():
    dado = request.json
    for car in db.carros:
        if car['id'] == dado['id'] or car['placa'] == dado['placa']:
            return {"msg": "Carro existente", 'status': 406}, 406
    
    db.carros.append(dado)
    return jsonify(dado), 201

@app.route("/carros", methods=["PUT"])
@cross_origin()
def altera_carro():
    dado = request.json
    for car in db.carros:
        if car['id'] == dado['id']:
            car['modelo'] = dado['modelo']
            car['montadora'] = dado['montadora']
            car['ano'] = dado['ano']
            car['placa'] = dado['placa']
            return (car, 200)
        
    return {'title': 'Carro not found', 'status': 404, 
            "type": "https://fiap.com.br/car_not_found", 
            "detail": f"Carro nao encontrado com o id especificado {dado['id']}", "instance": f"/carros/{dado['id']}"}, 404

@app.route("/carros/update", methods=["PUT"])
@cross_origin()
def altera_carro2():
    dado = request.json
    for ind, car in enumerate(db.carros):
        print(id, car)
        if car['id'] == dado['id']:
            db.carros[ind] = dado
            return dado, 200
    return {"title": "Carro não encontrado", "status": 404}, 404

@app.route("/carros/oracle", methods=["POST"])
@cross_origin()
def insere_carro_oracle():
    carro = request.json
    try:
        bc.insere(carro)
        return carro, 201
    except Exception as e:
        return {'title': 'Nao foi possivel inserir carro no banco', 'status': 500}, 500

@app.route("/carros/oracle/<int:id>", methods=["GET"])
@cross_origin()
def recupera_id_oracle(id):
    try:
        carro = bc.recupera_id(id) 
        if carro == None:
            return {'title': f'Não existe carro com o id: {id}', 'status': 404}, 404
        else:
            return (carro, 200)
    except Exception as e:
        return {'title': 'Erro no banco de dado', 'status': 500}, 500

@app.route("/carros/oracle", methods=["PUT"])
@cross_origin()
def altera_carro_oracle():
    carro = request.json
    bc.update(carro)
    return carro, 200

app.run(debug=True)
