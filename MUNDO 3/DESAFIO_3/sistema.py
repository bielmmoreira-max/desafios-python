from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
  criarArquivo(arq)

while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

  match resposta:
    case 1:
      lerArquivo(arq)

    case 2:
      cabecalho('NOVO CADASTRO')
      nome = str(input('Nome: '))
      idade = leiaInt('Idade: ')
      cadastrar(arq, nome, idade)

    case 3:
      cabecalho('Saindo do sistema... Até logo!')
      break

    case _:
      print('\033[31mERRO! Digite uma opção válida!\033[m')

  sleep(1)