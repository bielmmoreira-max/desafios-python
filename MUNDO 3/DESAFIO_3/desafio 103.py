def ficha(nome='<desconhecido>',gols=0):
    return f' O jogador {nome} fez {gols} gols'


n = str(input('Digite o nome do jogador: ')).strip()
g = str(input('Digite o numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    print(ficha(gols = g))
else:
    print(ficha(n,g))
