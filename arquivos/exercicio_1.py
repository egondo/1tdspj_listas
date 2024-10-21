import random

def cria_data(datas_criadas):
    data = ""
    while data == "" or data in datas_criadas: 
        dia = random.randint(1, 30)
        mes = random.randint(1, 12)
        if mes == 2 and dia > 28:
            dia = random.randint(1, 28)

        data = f"{dia}/{mes}/2023"
    datas_criadas[data] = data
    return data



lojas = ["Centro", "Jardins", "Tatuapé", "Saúde"]
produtos = [
    {"produto": "celular", "marca": "LG", "preco": 1378.99},
    {"produto": "celular", "marca": "Xiaomi", "preco": 958.39},
    {"produto": "celular", "marca": "Samsung", "preco": 1908.79},
    {"produto": "notebook", "marca": "DELL", "preco": 3299.00},
    {"produto": "notebook", "marca": "Acer", "preco": 2899.00},
    {"produto": "geladeira", "marca": "Panasonic", "preco": 5699.00},
    {"produto": "geladeira", "marca": "Brastemp", "preco": 3499.00},
    {"produto": "geladeira", "marca": "Electrolux", "preco": 4699.00},
    {"produto": "lavadora", "marca": "LG", "preco": 6250.00},
    {"produto": "lavadora", "marca": "Brastemp", "preco": 2450.00}
]

datas_geradas = {}

with open("dados_venda.txt", mode="w") as arq:
    i = 0
    while i < 5000:
        data_venda = cria_data(datas_geradas)
        for loja in lojas:
            for prod in produtos:
                arq.write(prod['produto'])
                arq.write(";")
                arq.write(prod['marca'])
                arq.write(";")
                arq.write(loja)
                arq.write(";")
                print(data_venda)
                arq.write(data_venda)
                arq.write(";")
                arq.write(str(random.randint(1, 20)))
                arq.write(";")
                arq.write(str(prod['preco']))
                arq.write("\n")
                i = i + 1