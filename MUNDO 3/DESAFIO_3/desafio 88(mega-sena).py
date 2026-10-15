from random import randint
jogos = list()
jogo = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, quant):
    while len(jogo) < 6:
      num = randint(1, 60)
      if num not in jogo:
        jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
