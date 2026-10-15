from datetime import date
def voto(a):
    idade = date.today().year - a
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano = int(input('Ano de nascimento: '))
print(voto(ano))