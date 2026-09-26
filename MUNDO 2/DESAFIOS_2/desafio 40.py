nm = str(input('Qual seu nome: '))
n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
m = (n1 + n2)/2

print(f'Sua media foi {m}')
if m >= 7:
    print(f'{nm} FOI APROVADO! ')
elif m < 5:
    print(f'\033[;31m{nm} REPROVADO! ')
else:
    print(f'{nm} esta de recuperação')