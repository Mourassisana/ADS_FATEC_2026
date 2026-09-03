# Exercício 2: Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%

# 1. Coleta o salário atual
Sal = float(input("Insira o valor do salário atual do funcionário: BRL "))

# 2. Calcula o novo salário aplicando o reajuste diretamente
Novo = (Sal * 1.15)

# 3. Exibe o salário reajustado com duas casas decimais (:.2f)
print(f"O salário pós reajuste é: BRL {Novo:.2f}")