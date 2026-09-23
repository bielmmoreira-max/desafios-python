l1 = float(input('digite o primeiro lado: '))
l2 = float(input('digite o segundo lado: '))
l3 = float(input('digite o terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Pode formar um triangulo')
else:
    print('\033[0;31mNão é possível formar um triangulo')