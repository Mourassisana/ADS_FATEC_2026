# Exercício 3: Receba a base e a altura de um triângulo. Calcule e mostre a sua área.

# 1. Recebe as duas dimensões
base = int(input("Insira o valor da base do triângulo: "))
altura = int(input("Insira o valor da altura do triângulo: "))

# 2. Calcula a área (base * altura)
area = ((base * altura) / 2)

# 3. Exibe o resultado
print(f"A área do triângulo é: {area:.0f}" )