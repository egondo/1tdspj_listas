try:
    a = int(input("A: "))
    b = int(input("B: "))
    c = a / b
except (ZeroDivisionError, ValueError) as e:
    if type(e) == ValueError:
        print("Erro de valor")
    else:
        print("Erro de divisao")
    #print("Erro", type(e))
    
else:
    print(f"Resultado divisao {c}")