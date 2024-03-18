preco = float(input("Informe o preço de etiqueta: "))
codigo = int(input("Opção de pagamento (1-4):"))

match codigo:
    case 1:
        novo_preco = preco - preco * 0.1    #ou nov_preco = preco * 0.9
        print(f"O valor a ser pago será de {novo_preco}")

    case 2:
        novo_preco = preco * 0.95
        print(f"O valor a ser pago será de {novo_preco}")
    
    case 3:
        parcela = preco / 2
        print(f"O valor a ser pago será de {preco} em 2x de {parcela}")

    case 4:
        novo_preco = preco * 1.07
        parcela = novo_preco / 4
        print(f"O valor a ser pago será de {novo_preco} em 4x de {parcela}")
    
    case _: #default = quando codigo não é nenhum das opções listadas
        print("Opção de pagamento inválida")

