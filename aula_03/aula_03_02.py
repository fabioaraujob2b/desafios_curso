idade = int(input("Informe sua idade: "))

if idade < 18:
    print(f"Você tem {idade} anos, acesso negado!")
elif idade >= 18 and idade < 65:
    print(f"Você tem {idade} anos, Acesso liberado!")
elif idade >= 65 and idade <= 100:
    print(f"Você tem {idade} anos, Acesso liberado!")
elif idade > 100:
    print(f"Você tem {idade} anos, Ainda está vivo?")
else:
    print(f"Você tem {idade} anos. Acesso liberado!")
