from time import sleep


def notas(*num, sit=False):
    """
    -> Função para realizar analises de várias notas do aluno indicando o total de notas
    , a maior e menor nota, média, e a situação caso queira.
    :param num: notas do aluno.
    :param sit: (opcional), de acordo com a análise feita nas notas indica a situação do aluno.
    :return: dicionario com todos os dados referidos.
    """
    med = sum(num) / len(num)
    nota = {'Total': len(num), 'Maior nota': max(num), ' nota': min(num), 'Média': med}
    if sit:
        if med <= 4:
            nota['Situação'] = 'Má'
        elif 4 < med <= 7:
            nota['Situação'] = 'Razoável'
        else:
            nota['Situação'] = 'Boa'
    return nota


# Programa principal
res = notas(0, 5, 7, 8.5, 0, sit=True)
print('Analisando...')
sleep(2)
print('+-' * 50)
print(res)
print('+-' * 50)
