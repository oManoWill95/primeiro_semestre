def diagnostico_clinico(temperatura, sintomas, historico, idade):
    sintomas = [s.strip().lower() for s in sintomas]  # Normaliza os sintomas para minúsculas e sem espaços
    historico = historico.lower().strip()  # Normaliza o histórico

    # Regra 1: Temperatura ≥ 39 e "tosse seca" e histórico → "Suspeita de COVID Grave"
    if temperatura >= 39 and "tosse seca" in sintomas and historico == "sim":
        return "Suspeita de COVID Grave"

    # Regra 2: "falta de ar" e temperatura ≥ 38 → "Emergência Respiratória"
    if "falta de ar" in sintomas and temperatura >= 38:
        return "Emergência Respiratória"

    # Regra 3: Temperatura < 35 e idade > 65 → "Hipotermia com Risco"
    if temperatura < 35 and idade > 65:
        return "Hipotermia com Risco"

    # Regra 4: "dor de cabeça" e "náusea" → "Suspeita de Enxaqueca"
    if "dor de cabeça" in sintomas and "náusea" in sintomas:
        return "Suspeita de Enxaqueca"

    # Caso contrário → "Avaliação Padrão"
    return "Avaliação Padrão"

def main():
    temperatura = float(input("Digite a temperatura corporal (30 a 45 °C): "))
    sintomas_input = input("Digite os sintomas (separe por vírgula, ex: tosse seca, falta de ar): ")
    sintomas = sintomas_input.split(",")
    historico = input("Possui histórico de doenças crônicas? (sim ou não): ")
    idade = int(input("Digite a idade: "))

    # Validação básica da temperatura
    if not (30 <= temperatura <= 45):
        print("Temperatura inválida! Deve estar entre 30 e 45 °C.")
        return

    diagnostico = diagnostico_clinico(temperatura, sintomas, historico, idade)
    print(f"Diagnóstico: {diagnostico}")

if __name__ == "__main__":
    main()
