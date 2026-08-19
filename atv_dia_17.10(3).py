i = 1
maior = None
menor = None

while i <= 10:
    num = int(input(f"Digite o {i}º número: "))

    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    i += 1

print("Maior número:", maior)
print("Menor número:", menor)
