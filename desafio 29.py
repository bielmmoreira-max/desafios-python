v = float(input('velocidade do carro: '))
multa = (v - 80)*7
if v > 80:
    print(f'\033[;31mPassou do limite de velocidade e pagará uma multa de {multa} reais')
else:
    print('Velocidade permitida')