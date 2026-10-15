def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return int(n)



def leiaFloat(msg):
  while True:
    try:
        entrada = input(msg).strip().replace(',', '.')
        n = float(entrada)
    except (ValueError, TypeError):
        print(f'\033[0;31mERRO: " é um número Real inválido!\033[m')
        continue
    except (KeyboardInterrupt):
        print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        return 0
    else:
        return n


num1 = leiaInt('Digite um valor Inteiro: ')
num2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')