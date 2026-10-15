matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
soma = 0
col = 0
for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    soma += matriz[l][c]
    if matriz[l][c] % 2 == 0:
        spar += matriz[l][c]

print(f'[{matriz[0]}\n[{matriz[1]}]\n[{matriz[2]}]')
print(f'A soma dos pares é {spar}')
print(f'A soma de todos os números é {soma}')
for l in range(0,3):
    col += matriz[l][2]
print(f'A soma da coluna 3 é {col}')
print(f'O maior valor da linha 2 é {max(matriz[1])}')