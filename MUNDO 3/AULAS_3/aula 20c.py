def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,5,3,9,2,1,10]
dobra(valores)
print(valores)