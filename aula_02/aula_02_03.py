#Entrada 
valor = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe o valor da taxa: "))
tempo = int(input("Informe o atraso em dias: "))

#processamento
juros = valor * (taxa/100) * tempo
resultado = valor + juros
#saída
print(f"Os juros da prestação são {juros:.2f}, portante o valor final a ser pago será: {resultado:.2f}")