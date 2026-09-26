p = float(input('Qual seu peso? '))
a = float(input('Qual sua altura? '))
imc = p/(a**2)
print(f'Seu imc é {imc}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')