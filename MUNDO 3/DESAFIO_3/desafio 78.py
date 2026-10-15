valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    if c == 0:
        maior = v
        menor = v
    if v > maior:
        maior = v
    if v < menor:
        menor = v
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição {valores.index(maior)+1}')
print(f'O menor valor digitado foi {menor} na posição {valores.index(menor)+1}')