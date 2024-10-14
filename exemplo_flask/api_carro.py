from flask import Flask, request, jsonify
import db

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def get_all_carros():
    return  (jsonify(db.carros), 200)

@app.route("/carros/<int:id>", methods=["GET"])
def get_carro(id):    
    #return str(id), 200
    for car in db.carros:
        if car['id'] == id:
            return jsonify(car), 200
    
    return {'msg': 'Nenhum carro encontrado', 'status':404}, 404

@app.route("/carros", methods=['POST'])
def insere_carro():
    dado = request.json
    for car in db.carros:
        if car['id'] == dado['id'] or car['placa'] == dado['placa']:
            return {"msg": "Carro existente", 'status': 406}, 406
    
    db.carros.append(dado)
    return jsonify(dado), 201

@app.route("/carros", methods=["PUT"])
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
def altera_carro2():
    dado = request.json
    for ind, car in enumerate(db.carros):
        print(id, car)
        if car['id'] == dado['id']:
            db.carros[ind] = dado
            return dado, 200
    return {"title": "Carro não encontrado", "status": 404}, 404



app.run(debug=True)
