temp = []
opcao = 0
maior = 0
menor = 0
media = 0
while True:
    print("Digite '1' para informar as temperaturas: ")
    print("Digite qualquer coisa para sair: ")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        temperatura = float(input("Digite a temperatura: "))
        temp.append(temperatura)
        print(f"\nTeperatura {temperatura} adicionada.")
    else:
        print("\nSaindo...")
        break

for i in range(len(temp)):
    if i == 0:
        maior = temp[i]
        menor = temp[i]
    else:
        if temp[i] > maior:
            maior = temp[i]
        if temp[i] < menor:
            menor = temp[i]

media = sum(temp) / len(temp)
print(f"\nA menor temperatura: {menor:.2f}°")
print(f"\nA maior temperatura: {maior:.2f}°")
print(f"\nA média final de temperatura: {media:.2f}°")

