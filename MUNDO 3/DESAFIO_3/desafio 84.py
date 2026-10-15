pessoas = list()
dados = list()
pesados = list()
leves = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont = str(input('Continuar? [S/N]')).upper().strip()
    if cont == 'N':
        break
mai = men = pessoas[0][1]
for p in pessoas:
    if p[1] > mai:
        mai = p[1]
    if p[1] < men:
        men = p[1]
for p in pessoas:
    if p[1] == mai:
        pesados.append(p[0])
    if p[1] == men:
        leves.append(p[0])
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}.e são {pesados}')
print(f'O menor peso foi de {men}.e são {leves} ')

