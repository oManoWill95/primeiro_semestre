def perfil_investidor(idade, renda_mensal, tolerancia_risco):
    tolerancia = tolerancia_risco.lower().strip()  # Normaliza a entrada

    if renda_mensal >= 10000 and tolerancia == "alta":
        return "Perfil Agressivo"
    elif renda_mensal >= 5000 and tolerancia == "média":
        return "Perfil Moderado"
    elif idade >= 60 and tolerancia == "baixa":
        return "Perfil Conservador"
    elif renda_mensal < 2000:
        return "Perfil Iniciante"
    else:
        return "Perfil Neutro"

def main():
    idade = int(input("Digite a idade do investidor: "))
    renda_mensal = float(input("Digite a renda mensal do investidor: "))
    tolerancia_risco = input("Digite a tolerância a risco (alta, média, baixa): ")

    perfil = perfil_investidor(idade, renda_mensal, tolerancia_risco)
    print(f"O perfil do investidor é: {perfil}")

if __name__ == "__main__":
    main()
