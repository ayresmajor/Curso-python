from datetime import date
pessoa ={'Nome': str(input('Nome: ')),
         'Idade': date.today().year - int(input('Ano de Nascimento: ')),
         'CTPS': int(input('Carteira de Trabalho (0 não tem): '))}
if pessoa['CTPS'] > 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    if date.today().year - pessoa['Contratação'] >= 35:
        pessoa['Aposentadoria'] = pessoa['Idade']
    else:
        pessoa['Aposentadoria'] = (35 - (date.today().year - pessoa['Contratação'])) + pessoa['Idade']
print('-=' * 25)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
