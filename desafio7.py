nm = str(input('nome do aluno:'))
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1+n2)/2

print(f'a media do aluno {nm} é {m}')
if m >= 7:
    print(f'o aluno {nm} foi aprovado! ')
else:
    print(f'o aluno {nm} foi reprovado')