# Exercício 16: Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário bruto (horas trabalhadas x valor por hora). Calcule o salário líquido. Exiba o salário a receber.

# 1. Recebe os valores iniciais
horas_trab = float(input("Insira a quantidade de horas trabalhadas: "))
valor_hora = float(input("Insira o valor recebido por hora: BRL "))
per_desc = float(input("Insira o percentual de desconto (somente números): %"))
dependentes = int(input("Insira a quantidade de dependentes: "))

# 2. Calcula o salário bruto, o valor do desconto e o acréscimo por dependente
sal_bru = (horas_trab * valor_hora)
valor_desc = (sal_bru * (per_desc / 100))
sal_liq = (sal_bru - valor_desc)

# 2.1. Calcula o salário final
valor_acr = (dependentes * 100)
sal_rec = (sal_liq + valor_acr)

# 3. Exibe resultados
print(f"\n--- Demonstrativo de Pagamento ---")
print(f"Salário Bruto: BRL {sal_bru:.2f}")
print(f"Desconto: BRL {per_desc:.2f}")
print(f"Acréscimo por dependente: BRL {valor_acr:.2f}")
print(f"Salário a Receber: BRL {sal_rec:.2f}")