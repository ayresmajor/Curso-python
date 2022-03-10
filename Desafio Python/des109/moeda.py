def aumentar(num, quant, form=True, moeda='€'):
    res = num + ((quant/100) * num)
    if form:
        return f'{num:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def diminuir(num, quant, form=True, moeda='€'):
    res = num - ((quant/100) * num)
    if form:
        return f'{num:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def dobra(num, form=True, moeda='€'):
    res = num * 2
    if form:
        return f'{num:.2f}{moeda}'.replace('.', ',')
    else:
        return res


def metade(num, form=True, moeda='€'):
    res = num / 2
    if form:
        return f'{num:.2f}{moeda}'.replace('.', ',')
    else:
        return res
