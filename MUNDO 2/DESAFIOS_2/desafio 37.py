i = int(input('Digite um numero inteiro:'))
e = int (input('Base de conversão\n1 para binário\n2 para octal\n3 para hexadecimal\n'))

if e == 1:
    print(f'Em binário é {bin(i)[2:]}')
elif e == 2:
    print(f'Em octal é {oct(i)[2:]}')
elif e == 3:
    print(f'Em hexadecimal é {hex(i)[2:]}')
else:
    print('\033[;31mINVALIDO')