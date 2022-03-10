from time import sleep
salario =  float(input('Quanto é o seu salário? '))
if salario > 1250:
    print('Parabéns, voçê teve um aumento de 10%, o seu salário será {:.2f}'.format(salario + (salario * 0.1)))
else:
    print('Parabéns, voçê teve um aumento de 15%, o seu salário será {:.2f}'.format(salario + (salario * 0.15)))
print('\033[1:33mTenha um bom dia!!')

