f = str(input('detector de palíndromos: ')).strip().upper()
p = f.split()
junto = ''.join(p)
inv = ''

for l in range(len(junto)-1,-1,-1):
    inv += junto[l]
print(f'O inverso de {junto} é {inv}')

if inv == junto:
  print('Temos um PALÍNDROMO!')
else:
  print('A frase digitada NÃO é um palíndromo!')
