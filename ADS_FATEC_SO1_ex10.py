# Exercício 10: Receba 2 números reais. Calcule e mostre e a diferença desses valores.

# 1. Recebe os números reais
NR1 = float(input("Insira o valor do primeiro número real: "))
NR2 = float(input("Insira o valor do segundo número real: "))

# 2. Calcula a diferença
dif = NR1 - NR2

# 3. Exibe o resultado com duas casas decimais
print(f"A diferença entre {NR1} e {NR2} é: {dif:.2f}")