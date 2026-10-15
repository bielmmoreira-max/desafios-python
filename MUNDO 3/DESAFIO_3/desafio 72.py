numext = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
num = int(input('Digite um numero entre 0 e 20: '))
if num < 0 or num > 20:
    num = int(input('Tente novamente.Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {numext[num]}')