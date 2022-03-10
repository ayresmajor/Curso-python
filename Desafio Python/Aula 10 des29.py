print('\033[1:33m = \033[m'*20)
velocidade = float(input('Qual foi a velocidade atingida pelo seu carro? '))

print('\033[1:33m - \033[m'*20)
multa = ( (velocidade - 80) * 7)
if velocidade<= 80:
    print('Parabéns vc não ultrapassou o limite de velocidade.')
else:
    print('\033[:31mVocê ultrapassou o limite de 80km/h irá receber uma multa de \033[1:33m{:.2f}€.'.format(multa))
