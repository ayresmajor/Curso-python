def contador(*num):
    tam = len(num)
    print(f'Recebi os valores: {num}, e ao todo são {tam} número(s)')
    print()


contador(4, 8, 6, 7)
contador(4, 8, 1, 7, 5)
contador(4, 7)
