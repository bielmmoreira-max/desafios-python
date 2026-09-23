dis = int(input('distancia em km ate onde quer ir: '))
if dis <= 200:
    print(f'o valor da viagem sera {dis * 0.5}')
else:
    print(f'o valor da viagem sera {dis * 0.45}')
