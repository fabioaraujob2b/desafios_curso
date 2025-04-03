#Programa para calcular média.

#Entrada de dados
nome = input("Digite o nome do estudante: ")
n1 = float(input(f"Informe a primeira nota do estudante {nome}: "))
n2 = float(input(f"Informe a segunda nota do estudante {nome}: "))
n3 = float(input(f"Informe a terceira nota do estudante {nome} "))
#Processamento de dados 
media = (n1 + n2 + n2) / 3

#Saída
print(f"A média final do aluno {nome}: {media:.1f}")


