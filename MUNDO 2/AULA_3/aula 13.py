i = int(input('Digite o numero inicial:'))
f = int(input('Digite o numero final:'))
p = int(input('Digite o numero de passo:'))
if i < f:
    for c in range(i, f+1,p):
        print(c)
else:
    for c in range(i, f-1, -p):
        print(c)
print('fim')