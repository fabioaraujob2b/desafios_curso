par = 0
impar = 0
num = []
lista_par = []
lista_impar = []
for i in range(10):
    num.append(int(input(f"Informe o Valor: ")))
    if num[i] % 2 != 0:
        impar += 1
        lista_impar.append(num[i])
    else:
        par += 1
        lista_par.append(num[i])
print("\nResultado: ")   
print(f"A quantidade de números pares: {par}, os números pares são: {lista_par}")
print(f"A quantidade de números impares: {impar}, os números pares são: {lista_impar}")
num.reverse()
print("\nLista em ordem reversa")
print(num)
print("\nLista em ordem crescente")
num.sort()
print(num)
