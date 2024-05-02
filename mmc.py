def mmc(a, b):
    x = b
    while x % a != 0:
        x = x + b
    return x


a = int(input("Informe a: "))
b = int(input("Informe b: "))

x = b

while x % a != 0:
    x = x + b

print(f"MMC de {a} e {b} vale {x}")

