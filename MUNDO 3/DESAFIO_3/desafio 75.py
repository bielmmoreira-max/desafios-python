n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('digite outro numero: '))
n4 = int(input('digite outro numero: '))
num = (n1,n2,n3,n4)
print(f'Você digitou os números {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece na posição {num.index(3)+1}')
else:
    print('Não tem nenhum 3')
print('Os valores pares digitados foram: ', end='')
for c in num:
  if c % 2 == 0:
    print(c , ',', end=' ')

