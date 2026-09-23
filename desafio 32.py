from datetime import date
d = int(input('digite um ano:'))
if d == 0:
    d = date.today().year
if d % 4 == 0 and d % 100 != 0 or d % 400 == 0:
    print(f' Ano {d} é bissexto')
else:
    print(f'\033[;31mano {d} não é bissexto')