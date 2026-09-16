pe = float(imput("valor")
cp = int (unput("qual forma de pagamento:"))

if cp == 1 
	result = pe - (pe * 0.1)

elifi cp == 2:
	result = pe - (pe * 0.05)

elifi cp == 3: 
	result = pe

elifi cp == 4: 
	result = pe + (pe * 10)

Else:
	print ("Código invalido")

print(f"voce irá pagar {result}")
