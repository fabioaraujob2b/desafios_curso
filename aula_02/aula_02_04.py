from datetime import datetime

ano = int(input("Informe o ano de nascimento: "))
idade = datetime.now().year - ano
print(f"Sudade idade é: {idade}")
