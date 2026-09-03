# Exercício 5: Receba os coeficientes A, B e C de uma equação do 2º grau (AX² + BX + C = 0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes reais)

# 1. Recebe os 3 coeficientes
COA = float(input("Insira o valor do coeficiente A: "))
COB = float(input("Insira o valor do coeficiente B: "))
COC = float(input("Insira o valor do coeficiente C: "))

# 2. Calcula o Delta usando potência (**)
delta = ((COB ** 2) - (4 * COA * COC))

# 3. Calcula as duas raízes usando potência de 0.5 como raiz
x1 = (- COB + (delta ** 0.5)) / (2 * COA)
x2 = (- COB - (delta ** 0.5)) / (2 * COA)

# 4. Exibe duas linhas de resposta, uma com cada raiz
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")