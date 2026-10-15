valor = int(input('Qual o valor que quer retirar: '))
while True:
    c50 = valor // 50
    sobrou = valor % 50
    if sobrou == 0:
        c20 = 0
        c10 = 0
        c1 = 0
        break
    c20 = sobrou // 20
    sobrou2 = sobrou % 20
    if sobrou2 == 0:
        c10 = 0
        c1 = 0
        break
    c10 = sobrou2 // 10
    sobrou3 = sobrou2 % 10
    if sobrou3 == 0:
        c1 = 0
        break
    c1 = sobrou3 // 1
    sobrou4 = sobrou3 % 1
    if sobrou4 == 0:
        break
print(f'Você rceber {c50} notas de R$50')
print(f'Você rceber {c20} notas de R$20')
print(f'Você rceber {c10} notas de R$10')
print(f'Você rceber {c1} notas de $1')
