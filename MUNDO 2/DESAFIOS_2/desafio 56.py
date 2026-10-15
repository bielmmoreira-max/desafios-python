sidd = 0
midd = 0
nmvelho = ''
totm = 0
for c in range(1,5):
    print(f'{c} pessoa')
    nm = str(input('digite seu nome: ')).strip()
    idd = int(input('digite sua idade: '))
    g = str(input('seu sexo(M/F): ')).upper().strip()
    if g == 'F' and idd < 20:
        totm += 1
    if g == 'M':
        if nmvelho == '' or idd > midd:
            midd = idd
            nmvelho = nm
    sidd += idd
media = sidd/4
print(f'A media de idade é {media}')
print(f'o total de mulheres menores de 20 anos é {totm}')
print(f'o homem mais velho é {nmvelho} com {midd} anos')

