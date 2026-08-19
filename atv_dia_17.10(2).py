i = 1
maior = 0

while i <= 10:
    altura = float(input(f"Digite a altura da pessoa {i}: "))
    if altura > maior:
        maior = altura
    i += 1

print("A maior altura é:", maior)
