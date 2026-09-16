cotacao = float(input("Cotação do dólar: "))

precos_dolar = []
for _ in range(10):
    valor = float(input("Preço em dólar: "))
    precos_dolar.append(valor)

precos_reais = []
for valor in precos_dolar:
    precos_reais.append(valor * cotacao)

print(precos_reais)
print(sum(precos_reais))
