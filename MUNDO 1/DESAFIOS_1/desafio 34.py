s = float(input('digite o seu salario '))

if s <= 1250:
    aum = s + (s * 15/100)
else:
    aum = s + (s * 10/100)
print(f'seu novo salário ér {aum}')