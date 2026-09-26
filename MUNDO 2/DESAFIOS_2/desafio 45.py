import random
j = int(input('Escolha\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\n'))
jokenpo = ['PEDRA','PAPEL','TESOURA']
escolha = random.randint(0,2)
print('JOKENPÔ....')
print(f'O computador escolheu {jokenpo[escolha]}')
print(f'Você escolheu {jokenpo[j]}')
if escolha == j:
    print(f'EMPATE')
elif (j == 0 and escolha == 2) or (j == 1 and escolha == 0) or (j == 2 and escolha == 1):
    print('VOCÊ VENCEU!')
else:
    print('O COMPUTADOR GANHOU')
