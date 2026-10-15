def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ')
    else:
        if p > 0:
            p = -p
            for c in range(i, f - 1, p):
                print(c, end=' ')


contador(1,10,1)
print()
contador(10,0,-2)
print()
print('Contador personalizado')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)