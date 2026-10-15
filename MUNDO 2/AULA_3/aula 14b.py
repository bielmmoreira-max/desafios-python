import random
r = 'S'
f = int(input('Você quer um dado até que numero: '))
while r == 'S':
    d = random.randint(1,f)
    print(f'O dado deu: {d}')
    r = str(input('Quer continuar?[S/N] ')).upper()
