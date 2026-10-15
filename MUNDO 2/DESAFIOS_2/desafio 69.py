maioridade = 0
hm = 0
mlh20 = 0
while True:
    n = str(input('Digite o seu nome: '))
    idd = int(input('digite sua idade: '))
    if idd >= 18:
        maioridade += 1
    g = str(input('Digite seu sexo [M/F]:')).upper().strip()
    if g == 'M':
        hm += 1
    if g == 'F' and idd < 20:
        mlh20 += 1
    conti = str(input('Quer continuar? [S/N]')).upper().strip()
    if conti == 'N':
        break
print(f'Tem {maioridade} pessoas maiores de 18 anos')
print(f'Tem {hm} homens')
print(f'Tem {mlh20} mulheres com menos de 20 anos')