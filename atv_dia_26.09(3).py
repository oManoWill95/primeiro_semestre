def verifica_triangulo(lado1, lado2, lado3):
    # Verifica se os lados formam um triângulo válido
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return False  # Lados precisam ser maiores que zero
    
    # As somas de dois lados precisam ser sempre maiores que o terceiro lado
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return True
    else:
        return False

def tipo_triangulo(lado1, lado2, lado3):
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    # Leitura dos lados do triângulo
    lado1 = float(input("Digite o comprimento do primeiro lado: "))
    lado2 = float(input("Digite o comprimento do segundo lado: "))
    lado3 = float(input("Digite o comprimento do terceiro lado: "))
    
    if verifica_triangulo(lado1, lado2, lado3):
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print(f"Os lados formam um triângulo do tipo {tipo}.")
    else:
        print("Os lados não formam um triângulo válido.")

# Executando o programa
main()
