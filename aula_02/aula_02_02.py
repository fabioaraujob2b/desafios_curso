#Calcula o peso ideal

nome = input("Informe seu nome: ")
sexo = input(f"Digite M ou m para masculino ou F e f para feminino: ")
altura = float(input(f"Sr(a) {nome} informe sua altura: "))


if sexo == "M" and "m":
    peso_ideal = (72.7 * altura) - 58
    print(f"Sr {nome} seu peso ideal é: {peso_ideal:.2f}")
elif sexo == "F" or "f":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Sra {nome} seu peso ideal é: {peso_ideal:.2f}")
else:
    print("Opção inválida")
