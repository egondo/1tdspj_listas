n = int(input("Informe a qtd de alunos: "))
soma = 0
contador = 0
while contador < n:
    nota = float(input("Informe a nota: "))
    soma = soma + nota        #soma += nota

    contador = contador + 1   #contador += 1
    

media = soma / n 
print(f"Na minha turma de {n} alunos a média foi {media}")






