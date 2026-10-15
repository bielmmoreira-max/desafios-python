n = int(input('Quantos números iniciais da sequência de fibonacci: '))
f1 = 1
f2 = 1
cont = 1
if n >= 1:
    print(1)
if n >= 2:
    print(1)
while cont < n - 1 :
    cont += 1
    f = f1 + f2
    f1 = f2
    f2 = f
    print(f)