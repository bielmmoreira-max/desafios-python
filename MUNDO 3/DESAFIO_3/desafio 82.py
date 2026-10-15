valores = list()
par = list()
impar = list()
while True:
    n = (int(input('Digite um valor: ')))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')