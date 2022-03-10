def aumentar(num, quant, form=True, moeda='€'):
    res = num + ((quant/100) * num)
    if form:
        return f'{res:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def diminuir(num, quant, form=True, moeda='€'):
    res = num - ((quant/100) * num)
    if form:
        return f'{res:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def dobra(num, form=True, moeda='€'):
    res = num * 2
    if form:
        return f'{res:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def metade(num, form=True, moeda='€'):
    res = num / 2
    if form:
        return f'{res:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def resumo(p, a=0, d=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR"}'.center(30))
    print('-' * 30)
    print(f'''Preço analisado:\t{p:.2f}€
Metade do preço:\t{metade(p)}
Dobro do preço:\t\t{dobra(p)}
{a}% de aumento:\t\t{aumentar(p,a)}
{d}% de redução:\t\t{diminuir(p,d)} '''.replace('.', ','))
    print('-' * 30)
