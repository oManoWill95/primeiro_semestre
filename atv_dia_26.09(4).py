def classificacao_risco(idade, valor_mercado, tipo):
    # Regra 1: Se o valor for > 100.000 e tipo for "luxo", risco é Alto
    if valor_mercado > 100000 and tipo.lower() == "luxo":
        return "Risco Alto"
    
    # Regra 2: Se o veículo tiver mais de 15 anos, risco é Alto
    if idade > 15:
        return "Risco Alto"
    
    # Regra 3: Se o tipo for "carga" e valor > 80.000, risco é Médio
    if tipo.lower() == "carga" and valor_mercado > 80000:
        return "Risco Médio"
    
    # Regra 4: Se o tipo for "passeio" e valor < 50.000, risco é Baixo
    if tipo.lower() == "passeio" and valor_mercado < 50000:
        return "Risco Baixo"
    
    # Caso contrário, risco é Moderado
    return "Risco Moderado"

# Função principal para testar
def main():
    idade = int(input("Digite a idade do veículo (em anos): "))
    valor_mercado = float(input("Digite o valor de mercado do veículo (em reais): "))
    tipo = input("Digite o tipo do veículo (passeio, carga, luxo): ").strip().lower()

    risco = classificacao_risco(idade, valor_mercado, tipo)
    print(f"A classificação de risco do veículo é: {risco}")

# Executando o programa
main()
