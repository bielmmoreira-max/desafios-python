num = [[],[]]
dados = list()
for c in range(0,7):
    dados = (int(input('Digite um numero: ')))
    if dados % 2 == 0:
        num[0].append(dados)
    if dados % 2 == 1:
        num[1].append(dados)

num[0].sort()
num[1].sort()

print(f'Os numero pares foram {num[0]}')
print(f'Os numeros pares foram {num[1]}')
