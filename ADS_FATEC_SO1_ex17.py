# Exercício 17: Calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o automóvel faz 12km/l. Receber o tempo de percurso e a velocidade média

# 1. Recebe as informações acerca da viagem
tempo = float(input("Insira, em horas, o tempo total do trajeto: "))
velo = float(input("Insira, em km/h, a velolcidade média da viagem: "))

# 2. Calculos da distância percorrida x autonomia do carro (12 km/l)
distancia = (tempo * velo)
litros = (distancia / 12)

# 3. Exibe resultados
print(f"\n--- Relatório de Consumo ---")
print (f"Distância percorrida: {distancia:.2f} km")
print (f"Combustível consumido: {litros:.2f} litros")