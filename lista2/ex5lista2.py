dias_uteis = int(input("Informe a qtd de dias úteis: "))

horas_trabalhadas = float(input("Horas trabalhadas: "))

salario_hora = float(input("Salário hora: "))

jornada = dias_uteis * 8

valor_hora_extra = 0.0

if horas_trabalhadas > jornada:
    #tenho horas extras para calcular
    horas_extras = horas_trabalhadas - jornada
    valor_hora_extra = horas_extras * salario_hora * 1.5
    horas_trabalhadas = jornada

salario = horas_trabalhadas * salario_hora + valor_hora_extra

print(f"Horas-extra: R${valor_hora_extra:.2f}")
print(f"Salário total: R${salario:.2f}")

