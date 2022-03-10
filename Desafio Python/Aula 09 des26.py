frase = str(input('Digite um frase ')).strip().lower()
print('Na sua frase "a" {} vez(es)'.format(frase.count('a')))
print('"a" aparece pela primeira vez em {}'.format(frase.find('a') + 1))
print('"a" aparece pela última vez em {}'.format(frase.rfind('a') + 1))
