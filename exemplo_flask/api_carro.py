from flask import Flask, request, jsonify
import db

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def get_all_carros():
    return  (db.carros, 200)

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



app.run(debug=True)