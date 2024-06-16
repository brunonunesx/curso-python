from datetime import date

atual = date.today().year
s = 0
a = 0
for c in range (0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    if (ano - atual <= 18):
        s = s + c
    if (ano - atual > 18): 
        a = a + c
print('O total de pessoas com de maior é de {}'.format(s))
print('O total de pessoa abaixo de 18 anos é {}'.format(a))