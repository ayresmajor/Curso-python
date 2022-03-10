from datetime import date
ano = int(input('Diga o seu ano de nascimento, atleta? '))
idade = date.today().year - ano
print('Voçê nasceu em {} logo voçê tem {} anos.'.format(ano, idade))
if idade <= 9:
    print('A sua categoria é \033[1:31mMIRIM')
elif idade <= 14:
    print('A sua categoria é \033[1:32mINFANTIL')
elif idade <= 19:
    print('A sua categoria é \033[1:33mJUNIOR')
elif idade <= 25:
    print('A sua categoria é \033[1:34mSÊNIOR')
else:
    print('A sua categoria é \033[1:35mMASTER')