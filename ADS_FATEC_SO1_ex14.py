# Exercício 14: Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo

# 1. Recebe os valores dos 2 ângulos conhecidos
angulo1 = int(input("Insira o valor do primeiro ângulo: "))
angulo2 = int(input("Insira o valor do segundo ângulo: "))

# 2. Calcula o 3º ângulo
angulo3 = (180 - (angulo1 + angulo2))

# 3. Exibe resultado
print(f"O valor do terceiro ângulo é: {angulo3:.1f}°")