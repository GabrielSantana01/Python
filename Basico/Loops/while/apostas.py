import random 

while True:
    while True:
        escolha = str(input('Qual é sua escolha: PAR ou IMPAR? ')).upper()
        if escolha in 'PARIMPAR':
            break
    n = int(input('insira um numero: '))
    random = random.randint(0,10)
    soma = n + random
    print(f'você escolheu {escolha} e o numero {n}, o PC escolheu {random}, a soma dos valores é {soma} que é ', end='')
    if soma % 2 == 0:
        if escolha == 'PAR':
            print('par Você ganhou!!!')
        else:
            print('par Você perdeu!!!')
        break
    else:
        if escolha == 'IMPAR':
            print('impar Você ganhou!!!')
        else:
            print('impar Você perdeu!!!')
        break 
