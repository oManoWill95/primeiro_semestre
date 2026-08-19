def prioridade_atendimento(idade, sintomas, pressao_arterial):
    sintomas = [s.strip().lower() for s in sintomas]  # Normaliza os sintomas para minúsculas e sem espaços

    # Regra 1: Pressão ≥ 180 ou sintomas incluem “dor no peito” → Prioridade Máxima
    if pressao_arterial >= 180 or "dor no peito" in sintomas:
        return "Prioridade Máxima"
    
    # Regra 2: Idade ≥ 65 e sintomas incluem “febre” → Alta Prioridade
    if idade >= 65 and "febre" in sintomas:
        return "Alta Prioridade"
    
    # Regra 3: Sintomas incluem “tontura” ou “fraqueza” → Prioridade Média
    if "tontura" in sintomas or "fraqueza" in sintomas:
        return "Prioridade Média"
    
    # Caso contrário → Baixa Prioridade
    return "Baixa Prioridade"

def main():
    idade = int(input("Digite a idade do paciente: "))
    sintomas_input = input("Digite os sintomas (separe por vírgula, ex: febre, tontura): ")
    sintomas = sintomas_input.split(",")  # Separa os sintomas por vírgula
    pressao_arterial = int(input("Digite a pressão arterial do paciente: "))

    prioridade = prioridade_atendimento(idade, sintomas, pressao_arterial)
    print(f"A prioridade de atendimento é: {prioridade}")

# Executar o programa
main()
