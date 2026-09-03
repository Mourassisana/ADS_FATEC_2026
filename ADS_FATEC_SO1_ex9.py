# Exercício 9: Receba 2 números inteiros. Calcule e mostre a soma dos quadrados.

# 1. Recebe os números inteiros
num_1 = int(input("Insira o primeiro número inteiro: "))
num_2 = int(input("Insira o segundo número inteiro: "))

# 2. Calcula a soma dos quadrados
soma_quad = ((num_1 * num_1) + (num_2 * num_2))

# 3. Exibe a soma dos quadrados
print(f"A soma dos quadrados de {num_1} e {num_2} é: {soma_quad}")