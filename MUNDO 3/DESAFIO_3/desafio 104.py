def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
