import math
catetoo = int(input('digite o cateto oposto: '))
catetoa = int(input('digite o cateto adjacente: '))
hipo = math.hypot(catetoo, catetoa)
print(f'a hipotenusa é {hipo}')