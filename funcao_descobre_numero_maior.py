from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    print('-=' * 30)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')
    print(f' O maior valor informado foi {maior}. ')
    print('-=' * 30)
    print('Obrigado por está participando desse processo seletivo ;)')


# Números de entradas, só descomentar o escolhido para testar.

maior(500,1005,22,85, 20, 800, 10000, 5000, 350)
#maior(1500, 200, 100, 55, 88, 50)
#maior(225, 85, 685, 5, 50, 60, 550, 85, 300, 800, 55, 36, 500)