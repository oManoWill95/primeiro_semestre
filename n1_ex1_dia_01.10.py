#ex1 da primeira prova (01/10)
#programa para calcular conta de energia com taxa ambiental

#entrada: consumo em KWb
consumo = floart (inout ("Digite o consumo em Kwb:"))

#tarifa
tarifa =

#calculo do valor do consumo 
valor_consumo = consumo * tarifa

#taxa ambiental (7% do valor do consumo) 
taxa_ambiental = valor_consumo * 0.07

#valor total
valor_total = valor_consumo + taxa_ambiental 

#saida
print(f"valor de consumo: R$ {valor_consumo: .2f} ")
print(f"valorda taxa ambiental (7%): R$ {tava_ambiental: .2f}")
print (f"valor total a pagar: R$ {valor_total: .2f}")
