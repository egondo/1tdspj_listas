import baralho

deck = baralho.cria('maco')

baralho.embaralha(deck)

mao_jog1 = baralho.distribui(deck, 2)
mao_jog2 = baralho.distribui(deck, 2)

mesa = baralho.distribui(deck, 5)

print("Jog 1", baralho.to_str_list(mao_jog1))

print("Mesa: ", baralho.to_str_list(mesa))

print("Jog2 ", baralho.to_str_list(mao_jog2))
