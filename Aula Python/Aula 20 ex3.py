def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [5, 6, 8, 1, 2]
dobra(valores)
print(valores)