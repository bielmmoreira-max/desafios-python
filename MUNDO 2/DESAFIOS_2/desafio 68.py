from random import randint
v = 0
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    jog = str(input('PAR ou IMPAR:')).upper().strip()
    jnum = int(input('Escolha o numero:'))
    comp = randint(1,10)
    SOMA = jnum + comp
    print(f"eu escolhi o numero {comp} e você escolheu {jnum} a soma foi de {SOMA}")
    print('Deu par' if SOMA % 2 == 0 else 'Deu impar')
    if jog == 'PAR':
        if SOMA % 2 == 0:
            print('Voce ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif jog == 'IMPAR':
        if SOMA % 2 == 0:
            print('Voce perdeu')
            break
        else:
            print('Voce ganhou')
            v += 1
    print('Vamos jogar novamente')
print(f'Você ganhou {v} vezes')