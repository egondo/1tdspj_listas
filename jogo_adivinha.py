# O programa consiste em fazer o usuário adivinhar um número sorteado
# com menos tentativas possíveis.
# O programa sorteia um número aleatório entre 1 e 1000 e a cada tentativa
# que o usuário faz para acertar o número ele informa se o número sorteado 
# é maior, menor ou igual ao número chutado. Você tem 10 chances para 
# acertar o número no máximo.

import random

num = random.randint(1, 1000)

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 1 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 2 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 3 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 4 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 5 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 6 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 7 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 8 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 9 tentativa")

chute = int(input("Informe um número: "))
if chute > num:
    print("Tente um número menor!")
elif chute < num:
    print("Tente um número maior!")
else:
    print("Você acertou na 10 tentativa")
