from random import randint
vezes = 1
comp = randint(0, 10)
print('vou pensar em um numero entre 0 e 10')
n = int(input('Em qual numero eu pensei? '))
print('PROCESSANDO...')
while n != comp:
    vezes += 1
    n = int(input('ERROU! Tente novamente\nEm qual numero pensei:'))
print(f'PARABENS VC ACERTOU! EU PENSEI NO NUMERO {comp}\nVocê tentou {vezes} vezes')
