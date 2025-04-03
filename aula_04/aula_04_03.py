media = 0
for i in range(2):
    nome = input("Informe o nome do aluno: ")
    nota1 = float(input(f"Digite a nota: "))
    nota2 = float(input(f"Digite a nota: "))
    media = (nota1 + nota2) / 2
    
    if media >= 70:
        print(f"O aluno: {nome} ficou com média {media:.1f} e ele ficou ATENDIDO")
    elif media >= 30 or media < 70:
        print(f"O aluno: {nome} ficou com média {media:.1f} e ele ficou PARCIALMENTE ATENDIDO")
    else:
        print(f"O aluno: {nome} ficou com média {media:.1f} e ele ficou NÃO ATENDIDO")
    




        

