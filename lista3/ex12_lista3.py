num = int(input("Digite o número: "))
num_bak = num

resp = ""

while num != 0:
    dig = num % 10
    resp = resp + str(dig)
    num = num // 10

if int(resp) == num_bak:
    print(f"{num_bak} é palindromo")
else:
    print(f"{num_bak} não é palindrome")    