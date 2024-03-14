avista = float(input("Valor à vista IPTU: "))
parcela = float(input("Valor da parcela: "))

relativo = avista / (parcela * 10)
desconto = (1 - relativo) * 100

print(f"O valor do desconto é {desconto:.2f}%")

