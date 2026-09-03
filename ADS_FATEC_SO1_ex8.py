# Exercício 8: Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a.m.

# 1. Recebe o valor inicial
valor_inicial = float(input("Insira o valor inicial do depósito em poupança: BRL "))

# 2. Calcula o valor após um mês de aplicação
valor_final = (valor_inicial * 1.013)

# 3. Exibe o valor final, após um mês aplicado
print(f"O valor final após 1 mês de rendimento a 1,13% am é: BRL {valor_final:.2f}")