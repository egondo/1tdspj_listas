from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/msg", methods=["GET"])
def hello():
    return "Ola Mundo!"



app.run(debug=True)