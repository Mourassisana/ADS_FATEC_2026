# Exercício 4: Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em Fahrenheit (F = (9 * C + 160) / 5)

# 1. Receba a temperatura em graus Celsius (°C)
celsius = float(input("Insira a temperatura em graus Celsius (°C): "))

# 2. Converte Celsius em Fahrenheit
fahrenheit = ((9 * celsius + 160) / 5)

# 3. Exibe temperatura convertida
print(f"{celsius:.2f}°C é igual a: {fahrenheit:.2f}°F")