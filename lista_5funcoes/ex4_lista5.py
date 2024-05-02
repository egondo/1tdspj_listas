def eh_perfeito(num):
    divisor = 1
    soma = 0
    while divisor < num:
        if num % divisor == 0:
            soma = soma + divisor
        divisor = divisor + 1
    
    if soma == num:
        return True
    else:
        return False
    
#main    
for x in range(1, 70001):
    if eh_perfeito(x):
        print(x)



