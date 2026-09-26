v = float(input('Qual o valor da casa? '))
p = int(input('Em quantos anos deseja pagar? '))
s = float(input('Qual o seu salário?'))

pm = p*12
vp = v/pm
sm = s* (30/100)

if vp > sm:
    print('\033[;31mNão é possível fazer o empréstimo, pois passa o limite do seu salário ')
else:
    print(f'APROVADO!Sua parcela fica: {vp} em {pm} meses')