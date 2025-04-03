ht = float(input("Informe a quantidade de horas trabalhadas: "))
vh = float(input("Informe o valor da hora trabalhada: "))
pd = float(input("Informe o percentual de desconto: "))

salario_bruto = ht * vh
desconto = (pd/100) * salario_bruto
salario_liquido = salario_bruto - desconto

print(f"O salário liquido é: {salario_liquido:,.2f}")