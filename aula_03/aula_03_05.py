#Escreva um programa que, dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"Primeiro número: {n1} é maior que Segundo número: {n2} é Terceiro número: {n3}")
elif n2 > n1 and n2 > n3:
    print(f"Segundo número: {n2} é maior que Primeiro número: {n1} é Terceiro número: {n3}")
elif n3 > n1 and n3 > n2:
    print(f"Terceiro número: {n3} é maior que Primeiro número: {n1} é Segundo número: {n2}")
else:
    print(f"Primeiro número: {n1}, Segundo número: {n2} é Terceiro: {n3} são iguais.")
