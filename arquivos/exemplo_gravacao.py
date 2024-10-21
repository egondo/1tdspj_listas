import random

def gera_DDD():
    num = random.randint(11, 86)
    return f"({num})"

def gera_Telefone():
    num = random.randint(1000000, 9999999)
    return f"9{num}"

pessoas = ["Ana", "Bia", "Sergio", "Edu", "Fabio", "Graca", "Pedro", "Sueli", "Lais", "Tomas"]
sobrenome = ["Silva", "Albuquerque", "Lopes", "Gonçalves", "Ribeiro", "Castro", "Kim", "Assis", "Feliciano"]

with open("cadastro.txt", mode="w") as arq:
    for i in range(1000):
        x = random.randint(0, len(pessoas) - 1)
        y = random.randint(0, len(sobrenome) - 1)

        arq.write(f"{pessoas[x]} {sobrenome[y]}; {gera_DDD()} {gera_Telefone()}\n")