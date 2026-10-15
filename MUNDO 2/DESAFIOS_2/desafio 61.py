primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = 1

while decimo <= 10:
     print(f'{primeiro}', end=' -> ')
     primeiro += razao
     decimo += 1

print('FIM')