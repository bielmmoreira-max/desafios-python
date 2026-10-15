nome = str(input('Qual seu nome? ')).upper().strip()
if nome == 'RIVALDO':
    print('\033[;31mte amo Rivaldo!')
    for c in range(1,4):
        print('<3')
print(f'bom dia,{nome}')