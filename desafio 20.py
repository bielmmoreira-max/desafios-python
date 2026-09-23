import random
a1 = input(' aluno numero 1: ')
a2 = input(' aluno numero 2: ')
a3 = input(' aluno numero 3: ')
a4 = input(' aluno numero 4: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('a ordem será')
print(lista)