n = int(input("Informe n: "))
while n <= 0:
    n = int(input("Inválido, digite novamente: "))

if n == 1 or n == 2:
    print("Fibonacci vale 1")
else:
    ant = 1
    atual = 1
    prox = ant + atual
    posicao = 3

    while posicao < n:
        ant = atual
        atual = prox
        prox = ant + atual
        posicao = posicao + 1

    print(f"Fibonacci vale {prox}")    

