p = float(input('Qual o valor do produto:'))
pc = p * 5/100
c = int(input('Qual o meio de pagamento:\n[1] À vista (dinheiro/cheque/pix)\n[2] À vista (cartão)\n[3] Em até 2x no cartão\n[4] 3x ou mais\n'))
if c == 1:
    print(f'O produto tem um desconto de 10% e fica {p-(pc*2)} ')
elif c == 2:
    print(f'O produto tem um desconto de 5% e fica {p-(pc)} ')
elif c == 3:
    print(f'Você pagará o valor normal sem juros {p}')
elif c == 4:
    print(f'O produto tem 20% de juros e valor ficará {p+(pc*4)}')
else:
    print('INVALIDO')