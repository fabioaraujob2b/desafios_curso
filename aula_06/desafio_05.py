#5- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a
#qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos (louros, castanhos, pretos)
#- idade
#Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

sexo = []
cor_olhos = []
cor_cabelos = []
idade = []
maior = 0
qtd_fem = 0
qtd_ind_olhos_verdes_louros = 0

for i in range(10):
    sexo.append(input("Digite 'F' para feminino ou 'M' para masculino: ").upper())
    cor_olhos.append(input("Digite 'A' para olhos azuis ou 'V' para verde ou 'C' para castanhos: ").upper())
    cor_cabelos.append(input("Digite 'L' para cabelos louros, 'C' para castanhos ou 'P' para pretos: ").upper())
    idade.append(int(input("Informe as idades: ")))

    if idade[i] > maior:
        maior = idade[i]
    if sexo[i] == 'F' and idade[i] >= 18 and idade[i] <= 35:
        qtd_fem += 1
    if cor_olhos[i] == 'V' and cor_cabelos[i] == 'L':
        qtd_ind_olhos_verdes_louros += 1

print(f"\nO habitante mais velho tem: {maior} anos.")
print(f"A quantidade de individuos do sexo feminino com idades entre 18 e 35 anos: {qtd_fem}")
print(f"A quantidade de individuos de cabelos loiros e olhos verdes: {qtd_ind_olhos_verdes_louros}")
