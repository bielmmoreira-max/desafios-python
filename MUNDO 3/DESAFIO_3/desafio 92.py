from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
idd = datetime.now().year - ano_nasc
pessoa['Idade'] = idd
pessoa['CTPS'] = int(input('Carteira de trabalho: '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    apos = pessoa['Ano de Contratação'] + 35
    pessoa['Aposentadoria'] = apos - ano_nasc
print(pessoa)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')

