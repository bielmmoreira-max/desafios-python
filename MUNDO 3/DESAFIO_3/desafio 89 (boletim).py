ficha = list()
m = list()
while True:
    nome = str(input('Aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], m])
    cont = str(input('Quer continuar?[S/N]')).upper().strip()
    if cont == 'N':
        break
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
  print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opc == 999:
        print('FINALIZANDO...')
        break

    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')