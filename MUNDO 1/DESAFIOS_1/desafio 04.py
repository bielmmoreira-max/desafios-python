n = input('Digite algo: ')

print('O tipo primitivo é:', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('Está em maiúsculas?', n.isupper())
print('Esta em minusculo? ', n.islower())
print('Esta capitalizada? ', n.istitle())