from time import  sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 50)
    print((f'Contagem de {inicio} até {fim} de {passo} em {passo}.'))
    sleep(2)
    if inicio <= fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
while True:
    print('-=' * 50)
    print('Agora é a sua vez!!')
    ini = int(input('Início: '))
    fi = int(input('Fim:    '))
    pas = int(input('Passo:  '))
    contador(ini, fi, pas)
    while True:
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO!! Responda somente com S ou N')
    if res == 'N':
        break
print('Obrigado e bye!!')
