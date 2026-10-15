import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen(
        'http://www.pudim.com.br',
        timeout=10
    )
except urllib.error.URLError as erro:
    print('Erro:', erro)
else:
    print('Site acessível!')
    print('URL final:', site.url)
    print('Código:', site.status)
    site.close()