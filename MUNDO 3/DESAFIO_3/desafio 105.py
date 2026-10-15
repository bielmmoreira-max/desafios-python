def notas(*n, sit=False):
    """-> Analisa notas e situações de vários alunos.
      :param n: uma ou mais notas dos alunos (aceita várias)
      :param sit: valor opcional, indicando se deve ou não adicionar a situação
      :return: dicionário com várias informações sobre a situação da turma.
      """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 8:
            r['situação'] = 'ótima'
        elif r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'razoável'
        elif r['media'] <= 4:
            r['situação'] = 'ruim'
    return r


resp = notas(5,8,9,sit=True)
print(resp)