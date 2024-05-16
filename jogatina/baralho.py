def cria(tipo):
    monte = []
    for valor in range(1, 14):
        monte.append( (valor, 'o') )
        monte.append( (valor, 'e') )
        monte.append( (valor, 'c') )
        monte.append( (valor, 'p') )
    #TODO crie os outros tipos de baralho (truco e 2macos)
    return monte

deck = cria('maco')
for card in deck:
    print(card)

