jogador = dict()
gols_total = 0
gols = list()
jogador['Nome'] = str(input('Nome: '))
jogador['Partidas'] = int(input('Partidas jogadas: '))
for g in range(0,jogador['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {g + 1}? ')))
jogador['Gols por partida'] = gols
jogador['Gols Total'] = sum(gols)
print('-'*30)
print(jogador)
print('-'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i, g in enumerate(gols):
  print(f'   => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {jogador['Gols Total']} gols.')