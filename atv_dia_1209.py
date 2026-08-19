
def calcular_notas(valor):
    notas = [100, 50, 10, 5, 1]
    resultado = {}

    valor_restante = valor  # manter o valor original para exibir no final

    for nota in notas:
        quantidade = valor_restante // nota
        valor_restante = valor_restante % nota
        resultado[nota] = quantidade

    return resultado

def main():
    valor = int(input("Digite o valor em reais: R$ "))
    notas_necessarias = calcular_notas(valor)

    print(f"Valor lido: R$ {valor}")
    for nota in sorted(notas_necessarias.keys(), reverse=True):
        print(f"notas de {nota}: {notas_necessarias[nota]}")

if __name__ == "__main__":
    main()
