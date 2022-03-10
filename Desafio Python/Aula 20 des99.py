from time import sleep
def maior(*num):
    print('-=' * 50)
    print('Analisando os valores...')
    if len(num) == 0:
        print('Foram informados 0 valores \nO maior de todos foi 0.')
    else:
        nmaior = num[0]
        for n in num:
            print(n, end=' ')
            sleep(0.5)
            if n >= nmaior:
                nmaior = n
        print(f'Foram digitados {len(num)} valores no total.')
        print(f'O maior de todos foi {nmaior}.')


maior(0, 5, 6, 9)
maior(1)
maior()
