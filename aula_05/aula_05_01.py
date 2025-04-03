nomes = "nome1, nome2, nome3, nome4"
nomes_listas = ["nome1", "nome2", "nome3", "nome4"]
lista_vazia = []
lista_vazia.append(nomes_listas)
num = []

for i in range(1, 5):
    n = int(input(f"Digite um valor {i}: "))
    num.append(n)

for i in range(len(num)):
    print(f"O número {num[i]} está na posição {i} da lista")

print(num)
print(nomes)
print(lista_vazia[0][2])