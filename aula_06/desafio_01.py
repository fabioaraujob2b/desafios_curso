sal_bruto = 0
sal_liquido = 0
irrf = 11
inss = 8
sindicato = 5
desconto = 0

salario_hora = float(input("Informe o valor por hora trabalhada: "))
num_horas_mes_trablhadas = int(input("Informe o número de horas trabalhadas no mês: "))
sal_bruto = salario_hora * num_horas_mes_trablhadas
desconto = irrf + inss + sindicato
imposto = (desconto/100) * sal_bruto
sal_liquido = sal_bruto - imposto

print(f"Seu salario bruto foi de : R$ {sal_bruto:.2f}")
renda = (irrf/100) * sal_bruto
print(f"Foi descontando: R$ {renda:.2f} de IRRF")
inss_des = (inss/100) * sal_bruto
print(f"Foi descontando: R$ {inss_des:.2f} de INSS")
sind = (sindicato/100) * sal_bruto
print(f"Foi descontando: R$ {sind:.2f} de Sindicato")
print(f"\nO salario líquido a receber R$ {sal_liquido:.2f}")