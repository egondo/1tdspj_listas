num = int(input("Digite o número: "))
num_bak = num

resp = 0

while num != 0:
    dig = num % 10
    resp = resp * 10 + dig
    num = num // 10

if resp == num_bak:
    print(f"{num_bak} é palindromo")
else:
    print(f"{num_bak} não é palindrome")    