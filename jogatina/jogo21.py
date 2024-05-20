import baralho as bar

def soma_pontos(mao):
    soma = 0
    for c in mao:
        if c[0] > 10:
            soma = soma + 10
        else:
            soma = soma + c[0]
    return soma

monte = bar.cria('maco')
bar.embaralha(monte)

mao_hum = bar.distribui(monte, 2)
mao_cpu = bar.distribui(monte, 2)

print(f"Você: {bar.to_str_list(mao_hum)}")
print(f"Pontos: {soma_pontos(mao_hum)}")
resp = input("Quer mais cartas (s/n)? ")
while resp == 's':
    c = bar.compra(monte)
    mao_hum.append(c)
    print(f"Você: {bar.to_str_list(mao_hum)}")
    print(f"Pontos: {soma_pontos(mao_hum)}")
    resp = input("Quer mais cartas (s/n)? ")

pontos_cpu = soma_pontos(mao_cpu)
while pontos_cpu < 16:
    mao_cpu.append(bar.compra(monte))
    pontos_cpu = soma_pontos(mao_cpu) 

print("CPU ", bar.to_str_list(mao_cpu))
print(f"Pontos: {soma_pontos(mao_cpu)}")

#Verificacao do ganhador da partida!


