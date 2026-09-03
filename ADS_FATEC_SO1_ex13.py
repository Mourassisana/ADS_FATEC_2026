# Exercício 13: Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50gr ao dia

# 1. Recebe a quantidade de alimento em quilos.
alimento_kg = float(input("Insira a quantidade em kg de alimento: "))

# 2. Converte quilos em gramas
quantidade_g = (alimento_kg * 1000)

# 3. Calcula os dias dividindo o total em gramas pelo consumo
dias = (quantidade_g / 50)

# 4. Exibe o resultado SEM casas decimais
print(f"O alimento durará {dias:.0f} dias")