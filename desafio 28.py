from random import randint
comp = randint(0, 5)
print('vou pensar em um numero entre 0 e 5')
n = int(input('Em qual numero eu pensei? '))
print('PROCESSANDO...')
if n == comp:
    print(f'PARABENS VC ACERTOU! EU PENSEI NO NUMERO {comp}')
else:
    print(f'\033[;31mERROU! eu pensei no numero {comp}')