import math

metros_quadrados = float(input("Informe os metros quadrados a ser pintado: "))

litros = metros_quadrados / 3
capacidade_lata = 18
latas_necessarias = math.ceil(litros/capacidade_lata) #
custo_lata = 130
custo_total = latas_necessarias * custo_lata

print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Custo total: R$ {custo_total:.2f}")
