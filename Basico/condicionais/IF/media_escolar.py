aluno = str(input('nome do aluno: '))
nota1semestre = float(input('insira a nota do primeiro semestre do aluno: '))
nota2semestre = float(input('insira a nota do segundo semestre do aluno: '))
media = (nota1semestre + nota2semestre)/2

if (media > 7.0) and (media <= 8.5):
    print(f'O aluno {aluno}teve a media de {media} de nota, Foi aprovado,', end ='')
    if nota1semestre < 7.0:
        print(' porem teve nota baixa no primeiro semestre')
    elif nota2semestre < 7.0:
        print('porem teve nota baixa no segundo semestre')
    else:
        print('sem resalvas')
if media > 8.5:
    print(f'O aluno {aluno}teve a media de {media} de nota, Foi aprovado,', end ='')
    if media == 10.0:
        print('o aluno tirou nota maxima')
    else:
        print('o aluno teve bom desempenho')
