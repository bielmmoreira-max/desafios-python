from random import randint
def sorteio(numeros):
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print(f'{numeros} números sorteado')


def somapar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares dos números sorteados é {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)