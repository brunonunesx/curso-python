from datetime import date

atual = date.today().year
ano = int(input('Qual é seu ano de nascimento? '))
idade = atual - ano 

print ('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if (idade == 18 ): 
    print('Você dever se alistar esse ano')
elif(idade > 18):
    q = idade - 18  
    print('Voce já passou {} anos do alistamento.'.format(q))
    alistamento = atual - q 
    print('Seu alistamento foi em {}'.format(alistamento))
else:
    q = 18 - idade
    print('Ainda falta {} anos para se alistar'.format(q)) 
    alistamento = atual + q
    print('Seu alistamento vai ser em {}'.format(alistamento))