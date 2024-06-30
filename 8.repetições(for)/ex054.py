from datetime import date

atual = date.today().year
s = 0
a = 0
for c in range (0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    if (atual - ano < 21):
        s += 1
    if (atual - ano >= 21): 
        a += 1
print('O total de pessoas que atigiram a maioridade é {}'.format(a))
print('O total de pessoa abaixo de 18 anos é {}'.format(s))