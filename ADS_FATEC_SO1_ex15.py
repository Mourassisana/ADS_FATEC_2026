# Exercício 15: Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hippotenusa

# 1. Recebe os valores dos dois catetos
cateto1 = float(input("Insira o valor do primeiro cateto: "))
cateto2 = float(input("Insira o valor do segundo cateto: "))

# 2. Calcula a soma dos catetos e a raiz quadrada
hipotenusa = (((cateto1 * cateto1) + (cateto2 * cateto2)) ** 0.5)

# 3. Exibe resultado
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")