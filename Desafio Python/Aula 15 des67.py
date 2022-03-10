print('Tabuada')
while True:
    print('=*=' * 15)
    num = int(input('Digite um número para saber a sua tabuada: '))
    print('=*=' * 15)
    if num < 0:
        break
    for mult in range(1,11):
        res = num * mult
        print(f'{num} x {mult} = {res}')
    if num < 0:
        break
print('Não realizamos de números negativos. Obrigado pela utilização!!')
