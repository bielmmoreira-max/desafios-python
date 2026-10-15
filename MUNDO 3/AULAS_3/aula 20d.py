def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')


soma(2,5)
soma(3,4,10)