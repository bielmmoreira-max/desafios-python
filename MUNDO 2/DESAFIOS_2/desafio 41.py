from datetime import date
ann = int(input('Qual o ano de nascimento?'))
idd = date.today().year - ann

print(f'O atleta tem {idd} anos')
if idd <= 9:
    print('Você é da categoria mirim')
elif idd <= 14:
    print('Você é da categoria infantil')
elif idd <= 19:
    print('Você é da categoria junior')
elif idd == 20:
    print('Você é da categoria senior')
elif idd > 20:
    print('Você é da categoria master')