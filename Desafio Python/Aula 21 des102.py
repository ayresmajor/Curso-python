def fatorial(num = 1, show = False):
    """
    -> Cálculo do fatorial de um número
    :param num: O número a ser calculado
    :param show: (Opcional) mostra o calculo se True
    :return: Retorna o valor do fatorial do num.
    """
    cal = 1
    for c in range(num, 0, -1):
        cal *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return cal


f1 = fatorial(5, True)
print(f1)
