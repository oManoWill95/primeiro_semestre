#ex3
def calcular_frete(peso):
    if peso <= 100:
        valor = peso * 2.0
    else:
        valor = 100 * 2.0 + (peso - 100) * 1.5
    return valor

# Exemplo de uso
p = float(input("Digite o peso da carga em kg: "))
print(f"Valor a ser pago: R$ {calcular_frete(p):.2f}")
