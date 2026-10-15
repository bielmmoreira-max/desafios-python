from datetime import date
maior = 0
menor = 0

for c in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Tem {maior} pessoas maiores de idade')
print(f'Tem {menor} pessoas menores de idade')
