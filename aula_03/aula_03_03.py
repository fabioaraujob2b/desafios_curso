#Calcula o peso ideal
nome = input("Informe seu nome: ")
sexo = input(f"Digite M ou m para masculino ou F e f para feminino: ").strip().upper()

if sexo == 'F':
    altura = float(input(f"Sr(a) {nome} informe sua altura: "))
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Sr(a) {nome} seu peso ideal é: {peso_ideal:.2f}')
elif sexo == 'M':
    altura = float(input(f"Sr(a) {nome} informe sua altura: "))
    peso_ideal = (72.7 * altura) - 58
    print(f'Sr {nome} seu peso ideal é: {peso_ideal:.2f}')
else:
    print('Opção inválida')

