def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if idade < 18:
        return f'Com {idade} anos: NÃO PODE VOTAR'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


# Programa Principal
print('-=' * 50)
ano = int(input('Ano de nascimento: '))
print(voto(ano))
