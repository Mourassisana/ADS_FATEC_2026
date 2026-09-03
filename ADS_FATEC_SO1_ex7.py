# Exercício 7: Receba os valores do comprimento, largura e altura de um paralelepipedo. Calcule e mostre seu volume.

# 1. Receba as 3 dimensões
comp = float(input("Insira o comprimento do paralelepípedo em cm: "))
larg = float(input("Insira a largura do paralelepípedo em cm: "))
altura = float(input("Insira o altura do paralelepípedo em cm: "))

# 2. Calcula o volume
volume = (comp * larg * altura)

# 3. Exibe o resultado
print(f"O volume do paralelepípedo é: {volume:.2f} cm cúbicos")