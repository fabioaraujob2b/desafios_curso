idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
horas_de_sono = float(input("Informe a quantidade de horas de sono: "))

if idade < 16 or idade > 69:
    print(f"Você não pode doar sangue, pois você tem {idade} anos e não atende os requistios para a doação.")
elif peso < 50:
    print(f"Você não pode doar sangue, pois você tem {peso:.2f}kg e está abaixo do autorizado")
elif horas_de_sono < 6:
    print(f"Você não pode doar sangue, pois você dormiu {horas_de_sono} hora de sono.")
else:
    print(f"Você tem {idade} anos, seu peso é {peso}kg e teve {horas_de_sono:.2f} horas de sono, então você atende todos os requitistos para a doação de sangue.")
    