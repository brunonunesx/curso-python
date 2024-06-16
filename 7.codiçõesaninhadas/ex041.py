from datetime import date

atual = date.today().year
ano = int(input('Em qual ano você nasceu '))
idade = atual - ano 

if (idade <= 9 ):
    print('Voce esta na categoria mirim ')
elif (idade <= 14 ):
    print('Voce esta na categoria infantil')
elif (idade <=  19):
    print('Voce esta na categoria junior')
elif (idade <=  25):
    print('Voce esta na categoria senior')
else:
    print('Voce esta na categoria master')