from datetime import date
print('\033[:33m=====\033[1:34mBem vindo ao serviço militar faça o seu registro\033[:33m=====\033[m')
print('\033[1mRegistro')
sexo = str(input('Qual é o seu sexo? ')).strip()
if sexo.lower() == 'masculino':
    ano = int(input('\033[1:32mQual é o seu ano de nascimento?\033[m '))
    atual = date.today().year
    idade = atual - ano
    print('Você tem {} anos em {}. '.format(idade, atual))
    if idade > 18:
        print('Já se passaram {} ano(s) do tempo que devia se alistar.'.format(idade - 18))
        print('O seu alistamento foi em {}.'.format(atual - (idade - 18)))

    elif idade < 18:
        print('Ainda falta {} ano(s) para o seu alistamento.'.format(18 - idade))
        print('O seu alistamento será em {}.'.format(atual + (18 - idade)))
    else:
        print('Está na alutura certa de alistar, aliste-se \033[1:31mAGORA.')
else:
    print('Você não é obrigada a realizar o alistamento.')

