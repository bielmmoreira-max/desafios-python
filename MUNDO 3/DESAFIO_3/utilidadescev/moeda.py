def dobro(num=0, formato=False):
    r = num * 2
    return r if formato is False else moeda(r)
def metade(num=0, formato=False):
    r = num/2
    return r if formato is False else moeda(r)
def aumentar(num=0,p=0, formato=False):
    por = num * (p / 100)
    r = num + por
    return r if formato is False else moeda(r)
def diminuir(num=0,p=0, formato=False):
    por = num * (p / 100)
    r = num - por
    return r if formato is False else moeda(r)
def moeda(num=0, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.', ',')
def resumo(num=0, paum=0, pdim=0):
  print('-' * 30)
  print('RESUMO DO VALOR'.center(30))
  print('-' * 30)
  print(f'Preço analisado: \t{moeda(num)}')
  print(f'Dobro do preço: \t{dobro(num, True)}')
  print(f'Metade do preço: \t{metade(num, True)}')
  print(f'{paum}% de aumento: \t{aumentar(num, paum, True)}')
  print(f'{pdim}% de redução: \t{diminuir(num, pdim, True)}')
  print('-' * 30)