def conversao_para_segundos(horas, minutos, segundos):
    # Converte as horas para segundos, os minutos para segundos e soma com os segundos fornecidos
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Testando a função
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

resultado = conversao_para_segundos(horas, minutos, segundos)
print(f"O total em segundos é: {resultado}")
