#4- Crie um programa que:
#1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
#2- Exiba a lista completa.
#3- Exiba o maior e o menor número da lista.
#4- Exiba a soma e a média de todos os números.

num = []

for i in range(2):
    n = int(input("\nDigite os números: "))
    num.append(n)

for i in range(len(num)):
    if i == 0:
        maior = num[i]
        menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
soma = sum(num)
media = sum(num) / len(num)

print(f"A lista de todos números digitados: {num}")
print(f"O menor número da lista: {menor}")
print(f"O maior número da lista: {maior}")
print(f"Resultado da soma de todos os números = {soma}")
print(f"A média de todos os números: {media:.2f}")