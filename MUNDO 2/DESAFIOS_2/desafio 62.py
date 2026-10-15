primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
mais = 10
tot = 0
while mais != 0:
    tot += mais
    while cont <= tot:
         print(f'{primeiro}', end=' -> ')
         primeiro += razao
         cont += 1
    mais = int(input('Mais? '))
print('FIM')