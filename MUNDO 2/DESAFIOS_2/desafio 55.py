maior = 0
menor = 0
for c in range(1,6):
    p = float(input('Digite o seu peso:'))
    if c == 1:
        maior = p
        menor = p
    if p > maior:
        maior = p
    elif p < menor:
        menor = p
print(f'o maior peso é {maior}')
print(f'o menor peso é {menor}')