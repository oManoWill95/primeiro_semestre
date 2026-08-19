def classificacao_risco_financeiro(score, divida, saldo, renda):
    # Regra 1: Dívida > 2×renda e saldo < 100 → "Inadimplente Crítico"
    if divida > 2 * renda and saldo < 100:
        return "Inadimplente Crítico"
    
    # Regra 2: Score < 400 ou dívida > 1.5×renda → "Alto Risco"
    if score < 400 or divida > 1.5 * renda:
        return "Alto Risco"
    
    # Regra 3: Score entre 400 e 700 e saldo < 500 → "Risco Médio"
    if 400 <= score < 700 and saldo < 500:
        return "Risco Médio"
    
    # Regra 4: Score ≥ 700 e saldo > 1000 → "Risco Baixo"
    if score >= 700 and saldo > 1000:
        return "Risco Baixo"
    
    # Caso contrário → "Risco Indefinido"
    return "Risco Indefinido"

def main():
    score = int(input("Digite o score de crédito (0 a 1000): "))
    divida = float(input("Digite a dívida total: "))
    saldo = float(input("Digite o saldo em conta: "))
    renda = float(input("Digite a renda mensal: "))

    # Validação básica do score
    if not (0 <= score <= 1000):
        print("Score inválido! Deve estar entre 0 e 1000.")
        return

    classificacao = classificacao_risco_financeiro(score, divida, saldo, renda)
    print(f"Classificação de risco financeiro: {classificacao}")

if __name__ == "__main__":
    main()
