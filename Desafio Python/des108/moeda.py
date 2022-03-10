def aumentar(num, quant):
    res = num + ((quant/100) * num)
    return res


def diminuir(num, quant):
    res = num - ((quant/100) * num)
    return res


def dobra(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res


def dinheiro(num, moeda='€'):
    return f'{num:.2f}{moeda}'.replace('.', ',')
