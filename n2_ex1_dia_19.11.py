total = 0
baixa = 0
adequada = 0
alta = 0

for dia in range(1, 31):
    qtd = int(input(f"Dia {dia} - Quantidade de pães: "))
    total += qtd

    if qtd <= 800:
        baixa += 1
    elif qtd <= 1200:
        adequada += 1
    else:
        alta += 1

media = total / 30

print("Média diária:", media)
print("Dias de baixa produção:", baixa)
print("Dias de produção adequada:", adequada)
print("Dias de produção alta:", alta)
