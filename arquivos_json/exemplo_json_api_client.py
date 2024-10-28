import requests
import json

url = "http://127.0.0.1:5000/midias/3"

resposta = requests.get(url)
if resposta.status_code == 200:
    #print(resposta.json())
    with open('filmes.json', mode="w") as arq:
        json.dump(resposta.json(), arq, indent=3)
else:
    print("deu erro")