def maior(*num):
    if len(num) == 0:
        print('-'*30)
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        print('-'*30)
        print(f'{num} foram analisados {len(num)}\nO maior numero é {max(num)}')


maior(3,4,5,7,10,2)
maior(0,1,9)
maior(2,1)
maior(6)
maior( )