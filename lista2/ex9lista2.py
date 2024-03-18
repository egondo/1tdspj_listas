num_a = float(input("Informe um número"))
op = input("Operador: ")
num_b = float(input("Informe outro número"))

if op == '+':
    resultado = num_a + num_b
elif op == '-':
    resultado = num_a - num_b
elif op == '*':        
    resultado = num_a * num_b    
elif op == '/':
    if num_b != 0:
        resultado = num_a / num_b
    else:
        print("Não é possível resolver divisão por 0")
        resultado = "Error"
else:
    print("Operador invalido")
    resultado = "Error"

print(f"{num_a} {op} {num_b} = {resultado}")
