time = list()

while True:
  jogador = dict()
  gols = list()

  jogador['Nome'] = str(input('Nome: '))
  jogador['Partidas'] = int(input('Partidas jogadas: '))

  for g in range(0, jogador['Partidas']):
    gols.append(int(input(f'   Quantos gols na partida {g + 1}? ')))

  jogador['Gols por partida'] = gols[:]
  jogador['Gols Total'] = sum(gols)

  time.append(jogador.copy())

  while True:
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')

  if cont == 'N':
    break

print('-=' * 30)
print(f'{"cod":<4} {"Nome":<15} {"Gols":<15} {"Total":<5}')
print('-' * 40)

for k, v in enumerate(time):
  print(
      f'{k:<4} {v["Nome"]:<15} {str(v["Gols por partida"]):<15} {v["Gols Total"]:<5}'
  )
print('-=' * 30)

while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))

  if busca == 999:
    break

  if busca >= len(time) or busca < 0:
    print(f'ERRO! Não existe jogador com código {busca}!')
  else:
    print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
    for i, g in enumerate(time[busca]['Gols por partida']):
      print(f'    No jogo {i + 1} fez {g} gols.')

  print('-' * 40)

print('<< VOLTE SEMPRE >>')