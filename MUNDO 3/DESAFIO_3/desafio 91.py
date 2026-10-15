from random import randint
from operator import itemgetter
players = dict()
for c in range(0,4):
    sort = randint(1,6)
    players[f'Player {c+1}'] = sort
print('valores sorteados:')
for k,v in players.items():
    print(f'O jogado{k} tirou {v} ')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('Ranking:')
for i, v in enumerate(ranking):
  print(f'{i+1}° lugar: {v[0]} com {v[1]}')
