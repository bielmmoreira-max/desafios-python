times = (
    'Flamengo',
    'Palmeiras',
    'Atlético-MG',
    'Fortaleza',
    'Fluminense',
    'Athlético-PR',
    'Internacional',
    'Bragantino',
    'São Paulo',
    'Botafogo',
    'Vasco da Gama',
    'Cruzeiro',
    'Grêmio',
    'Corinthians',
    'Bahia',
    'Cuiabá',
    'Goiás',
    'Coritiba',
    'América-MG',
    'Santos',
)
print(f'A) Os 5 primeiros classificados são {times[0:5]} ')
print(f'B) Os 4 ultimos são {times[-1:-5:-1]}')
print(f'C) Os times em ordem alfabetica {sorted(times)}')
print(f'D) O Bragantino esta na posição {times.index('Bragantino')+1}')
