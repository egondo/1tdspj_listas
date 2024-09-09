try:
    a = int(input("A: "))
    b = int(input("B: "))
    c = a / b
except ZeroDivisionError:
    print("Denominador nao pode ser zero!")
else:
    print(f"Resultado divisao {c}")