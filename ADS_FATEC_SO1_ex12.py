# Exercício 12: Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

# 1. Recebe valores inteiros para ano de nascimento e ano atual
nascimento = int(input("Insira o ano de seu nascimento: "))
ano_atual = int(input("Insira o ano atual: "))

# 2. Calcula a diferença entre os anos e acrescenta 17
idade_atual = (ano_atual - nascimento)
idade_futura = (idade_atual + 17)

# 3. Exibe resultados
print(f"Sua idade atual: {idade_atual} anos")
print(f"Daqui 17 anos você terá: {idade_futura} anos")