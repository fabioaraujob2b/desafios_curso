nome = ["João Pé de Couves", "Anotônio Magalhães", "Marina Torres"]
numero = [10, 30, 50]
contador = [0, 0, 0]

for i in range(10):
    opcao = int(input("\nDigite o número do candidato: "))
    if opcao in numero:
        indice = numero.index(opcao)
        contador[indice] += 1
    else:
        print("\nNúmero inválido! Voto ignorado")

for i in range(len(nome)):
    print(f"\n{nome[i]} recebeu {contador[i]} votos.")

max_votos = max(contador)
indice_vencedor = contador.index(max_votos)

print(f"\nO vencedor é {nome[indice_vencedor]} com {max_votos} votos.")