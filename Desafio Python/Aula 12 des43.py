print('\033[1:mIndice de massa corporal')
peso = float(input('Qual o seu peso (kg) ? '))
altura = float(input('Qual a sua altura (m) ? '))
imc = peso / (altura**2)
print('Você tem {} kilos, mede {} metros e apresenta um IMC de {:.2f}.'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está \033[1:33mABAIXO DO PESO\033[m ideal.')
elif imc <= 25:
    print('Você está \033[1:32mNO PESO IDEAL.\033[m')
elif imc <= 30:
    print('Você está \033[1:36mACIMA DO PESO\033[m ideal. ')
elif imc <= 40:
    print('Você está na \033[1:35mOBESIDADE.\033[m')
else:
    print('Você está na \033[1:31mOBESIDADE MÓRBIDA.\033[m')

