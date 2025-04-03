#Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo
#que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado
#GABARITO com as seguintes respostas: A, B, B, D, E

gabarito = ['A', 'B', 'B', 'D', 'E']
resposta = []
pontos = 0
erros = 0
for i in range(5):
    resposta.append((input(f"Informe a opções da questão: ")).upper())
    
for i in range(len(resposta)):
    if gabarito[i] != resposta[i]:
        erros += 1
    else:
        pontos += 1

print(f"\nVocê acertou {pontos} e errou {erros}")
print(f"\nSuas respostas {resposta}")
print(f"\nGabarito {gabarito}")