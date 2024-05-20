import random

def cria(tipo):
    monte = []
    for valor in range(1, 14):
        monte.append( (valor, '♦') )
        monte.append( (valor, '♥') )
        monte.append( (valor, '♠') )
        monte.append( (valor, '♣') )
    
    if tipo == 'truco':
        i = 0
        while i < 12:
            monte.pop(28)
            i = i + 1
        #for i in range(12):
        #   monte.pop(32)
    if tipo == '2macos':
        monte = monte + monte

    return monte

def to_str(carta):
    if carta[0] == 1:
        return f"A{carta[1]}"
    elif carta[0] == 11:
        return f"J{carta[1]}"
    elif carta[0] == 12:
        return f"Q{carta[1]}"
    elif carta[0] == 13:
        return f"K{carta[1]}"
    else:
        return f"{carta[0]}{carta[1]}"

def compra(monte: list):
    if len(monte) > 0:
        return monte.pop()
    else:
        return None

def distribui(monte: list, qtd: int):
    mao = []
    for _ in range(qtd):
        mao.append(compra(monte))
    return mao

def embaralha(monte: list):
    for _ in range(500):
        i = random.randint(0, len(monte) - 1)
        j = random.randint(0, len(monte) - 1)
        aux = monte[i]
        monte[i] = monte[j]
        monte[j] = aux
    #random.shuffle(monte)

def to_str_list(mao: list):
    saida = ""
    for carta in mao:
        saida = f"{saida} {to_str(carta)}"
    return saida


if __name__ == "__main__":
   deck = cria('maco')
   #for card in deck:
   #    print(to_str(card))
   embaralha(deck)
   c = compra(deck)
   while c != None:
       print(to_str(c))
       c = compra(deck)
