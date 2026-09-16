total = 0
cont = 0

while True:
    paginas = int(input("Páginas lidas: "))
    if paginas == 0:
        break
    total += paginas
    cont += 1

if cont > 0:
    media = total / cont
else:
    media = 0

print("Total de páginas:", total)
print("Média de páginas:", media)
