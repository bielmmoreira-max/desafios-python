totg = 0
maismil = 0
nmbarato = ''
maisbarato = 0
while True:
    nm = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: '))
    if nmbarato == '' or maisbarato > valor:
        nmbarato = nm
        maisbarato = valor
    if valor >= 1000:
        maismil += 1
    totg += valor
    conti = str(input('Quer continuar? [S/N]')).upper().strip()
    if conti == 'N':
        break
print(f'O total de gasto de compras foi {totg}')
print(f'O totas de produtos com mais de mil reais é {maismil}')
print(f'O produto mais barato foi {nmbarato}')