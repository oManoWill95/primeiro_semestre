def celsius_para_fahrenheit(celsius):
    # Aplica a fórmula de conversão de Celsius para Fahrenheit
    fahrenheit = celsius * (9.0 / 5.0) + 32.0
    return fahrenheit

# Testando a função
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
