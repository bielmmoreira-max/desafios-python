frase = str(input('digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes')
print(f'a primeira letra A aparece na posição {frase.find('A')+1}')
print(f'a ultima letra A aparece na posição {frase.rfind('A')+1}')
