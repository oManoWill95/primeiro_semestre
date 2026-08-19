# Exercicio 1
# Um fabricante vendeu 120 unidades de um produto que custa R$40,00 cada. Sobre o
# valor vendido, o fabricante paga 40% de imposto. Escreva um programa que calcule o valor
# de imposto a ser pago.

quantidade = int(input('Digite a quantidade de produtos:'))
preco_unitario = float (input('Digite o preço unitário:'))
taxa_imposto = int (input('Digite a taxa de imposto:'))

valor_total = quantidade * preco_unitario
total_imposto = valor_total * taxa_imposto / 100

print('total de imposto:' , total_imposto)
print('valor total:' , valor_total)
