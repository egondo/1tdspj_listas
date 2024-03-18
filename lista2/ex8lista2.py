idade = int(input("Informe a idade do nadador: "))

if idade < 5:
    print("Não possui categoria!")

elif idade <= 7:
    print("Categoria: infantil")

elif idade <= 10: 
    print("Categoria: juvenil")

elif idade <= 15:
    print("Categoria: adolescente")

elif idade <= 30:
    print("Categoria: adulto")

elif idade > 30:
    print("Categoria: Sênior")                

