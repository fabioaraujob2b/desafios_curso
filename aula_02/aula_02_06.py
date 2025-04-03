tempo = float(input("Informe o tempo pecorrido: "))
distancia = float(input("Informe a distancia: "))

#Calcula a velocidade média
vm = distancia / tempo
consumo = distancia / 12

#Saída
print(f"A velocidade média: {vm:.0f} km/h")
print(f"Durante a viagem foi consumido {consumo:.2f} litros de combustível")