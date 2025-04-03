num = [10,2,3,5,6,20,50,77,4,1,15]
maior = max(num)
menor = min(num)
soma = sum(num)
media = soma / len(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print("O resultado da soma:", sum(num))
print(f"Maior {maior}, Menor {menor}")
print(f"Média: {media:.2f}")

