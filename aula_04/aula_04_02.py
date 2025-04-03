soma = 0
idade_mais_velho = 0
menor_idade = 9999
for i in range(2):
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Informe a idade: "))
    if idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if idade < menor_idade:
        menor_idade = idade
        nome_mais_novo = nome
    soma += idade

media = soma / (i+1) 

print(f"A soma das idades é: {soma}")
print(f"A média de idade é: {media:.1f} anos")
print(f"{nome_mais_velho} é o mais velho é ele tem {idade_mais_velho} anos de idade")
print(f"{nome_mais_novo} é o mais novo é ele tem {menor_idade} anos de idade")