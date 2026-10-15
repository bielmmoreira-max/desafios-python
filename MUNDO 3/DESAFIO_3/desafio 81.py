valores = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado. Tente novamente')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
valores.sort(reverse=True)
print(f'A) Foram digitados {len(valores)} valores')
print(f'B) Os valores são {valores} em decrescente')
if 5 in valores:
    print(f'O valor 5 foi digitado na lista na posição {valores.index(5) + 1}')
else:
    print('O VALOR 5 NÃO foi digitado na lista')