nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
total = len(nome) - nome.count(' ')
print(f'o total de letras no seu nome é: {total} ')
separado = nome.split()
print(f'o total de letras do seu primeiro é: {len(separado[0])}')