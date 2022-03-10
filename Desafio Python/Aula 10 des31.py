num = float(input('Qual é a distância da viagem em Km? '))
print('Bom dia viajante!!')
if num >200:
    print('Para uma viagem de {:.2f}Km de distância \nterá de pagar \033[1m{:.2f}€\033[m'.format(num, num * 0.45))
else:
    print('Para uma viagem de {:.2f}Km de distância \nterá de pagar \033[1m{:.2f}€\033[m'.format(num, num * 0.5))