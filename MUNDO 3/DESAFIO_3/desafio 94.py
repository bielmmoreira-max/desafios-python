galera = list()
somaidade = 0
mulheres = list()
while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper().strip()
    if pessoa['Sexo'] in 'MmFf':
        print('Cadastrado com sucesso')
    else:
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper().strip()
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    galera.append(pessoa.copy())
    cont = str(input('Quer continuar? [S/N]')).upper()
    if cont == 'N':
        break
print('-=' * 30)
print(f'A) Foram cadastrados {len(galera)} pessoas.')
for p in galera:
    somaidade += p['Idade']
media =  somaidade/len(galera)
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres} ')
print('D) Lista das pessoas que estão acima da média:')
for p in galera:
  if p['Idade'] > media:
    print(f'   => {p["Nome"]} com {p["Idade"]} anos.')
