from datetime import date
nm = str(input('Qual o seu nome?'))
ann = int(input('qual o ano de nascimento?'))
idd = date.today().year - ann

if idd < 18:
    print(f'Ainda não precisa se alistar {nm}')
elif idd == 18:
    print(f'{nm} esta na hora de se alistar')
else:
    print('Já passou da hora de se alistar')