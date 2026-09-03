# Exercício 6: Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

# 1. Recebe os valores de x e y, sendo possível receber números ou textos.
x = input("Insira o valor de x, sendo números ou textos: ")
y = input("Insira o valor de x, sendo números ou textos: ")

# 2. Efetuando a troca de conteúdos
temp = x
x = y
y = temp

# 3. Exibe o conteúdo trocado
print(f"O conteúdo de x após a troca é: {x}")
print(f"O conteúdo de y após a troca é: {y}")