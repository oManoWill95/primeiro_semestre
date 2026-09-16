#ex2
# Programa para calcular a duração de um evento esportivo

# Entrada
hora_inicio = int(input("Digite a hora de início (0-23): "))
hora_fim = int(input("Digite a hora de término (0-23): "))

# Cálculo da duração
if hora_fim >= hora_inicio:
    duracao = hora_fim - hora_inicio
else:
    duracao = (24 - hora_inicio) + hora_fim

# Saída
print(f"Duração do evento: {duracao} hora(s)")

# Verificação de alerta
if duracao > 12:
    print("⚠️ Alerta: o evento durou mais que o esperado (acima de 12h).")

if duracao == 0:
    print("Obs: duração considerada 24 horas.")
