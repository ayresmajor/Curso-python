print('\033[7:30m Cálculo da média do aluno.\033[m ')
nota1 = float(input('Digite a sua primeira nota. '))
nota2 = float(input('Digite a sua segunda nota. '))
med = (nota1 + nota2) / 2
print('A sua média foi {:.1f}'.format(med))
if med < 8:
    print('\033[1:31mREPROVADO!!\033[m vai estudar MAIS!!')
elif med < 9.9:
    print('Safou, você tem direito a recuperação')
else:
    print('PARABÉNS, você foi aprovado.')
