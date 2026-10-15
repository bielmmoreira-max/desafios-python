nuk = [2,5,9,1]
nuk.append(7)
nuk.insert(2,2)
nuk.sort(reverse=True)
if 5 in nuk:
    nuk.remove(5)
else:
    print('Não há 5 na lista')
print(*nuk,sep=',')
print(f'A lista tem {len(nuk)} elementos')