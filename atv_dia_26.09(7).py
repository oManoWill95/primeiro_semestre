def classificacao_climatica(temperatura, umidade, vento):
    # Verifica as condições em ordem de prioridade

    if temperatura > 35 and umidade < 30:
        return "Alerta de Onda de Calor"
    elif temperatura < 5 and vento > 30:
        return "Alerta de Frio Intenso"
    elif umidade > 90:
        return "Alerta de Tempestade"
    elif vento > 50:
        return "Alerta de Ventania"
    else:
        return "Clima Normal"

def main():
    temperatura = float(input("Digite a temperatura em °C: "))
    umidade = float(input("Digite a umidade em %: "))
    vento = float(input("Digite a velocidade do vento em km/h: "))

    classificacao = classificacao_climatica(temperatura, umidade, vento)
    print(f"Classificação do clima: {classificacao}")

if __name__ == "__main__":
    main()
