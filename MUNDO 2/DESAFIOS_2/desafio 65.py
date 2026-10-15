n = 0
cont = 0
soma = 0

r = 'S'
while r == 'S':
    n = float(input('Digite um numero: '))
    if cont == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont+=1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
print(f'A media foi {soma/cont}')
print(f'O maior número foi {maior} e o menor {menor}')