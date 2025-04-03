n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
    soma = n1 + n2
    print(f"A soma de {n1} + {n2} = {soma}")
elif n1 < n2:
    print(f"{n2} é maior que  {n1}")
    soma = n1 + n2
    print(f"A soma de {n2} + {n1} = {soma}")
else:
    print(f"{n1} é igual o {n2}")
    mult = n1 * n2
    print(f"A mutiplicação de {n1} x {n2} = {mult}")