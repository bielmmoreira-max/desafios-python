valores = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado. Tente novamente')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
valores.sort()
print(f'Os valores são {valores}')