from random import randint
ale = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
maior = ale[0]
menor = ale[0]
print(f'os valores sorteados são {ale}', end='')
for c in ale:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'\nO maior numero foi {maior}')
print(f'O menor numero foi {menor}')
