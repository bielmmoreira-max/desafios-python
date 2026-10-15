vezes = 0
soma = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    soma += n
    vezes += 1
    print('Digite 999 para parar.')
print(f'A soma dos {vezes} tudo foi {soma}')