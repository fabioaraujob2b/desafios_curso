import math

valor = int(input("Digite um valor: "))

resultado1 = math.pow(valor, 2)
resultado2 = math.pow(valor, 3)

print(f"O valor {valor} ao quadrado é: {resultado1:.0f}")
print(f"O valor {valor} ao cubo é: {resultado2:.0f}")