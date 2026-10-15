n = int(input('Digite um valor: '))
n2 = int(input('Digite outro numero: '))
opc = 0
while opc != 5:
    opc = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair'))
    if opc == 1:
        print(f'A soma dos números é {n + n2}')
    elif opc == 2:
        print(f'O resultado é {n * n2}')
    elif opc == 3:
        if n > n2:
            print(f'O maior número é {n}')
        else:
            print(f'O maior número é {n2}')
    elif opc == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')