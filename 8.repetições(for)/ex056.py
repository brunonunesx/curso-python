s = 0
maior = 0 
mulher = 0 
nomevelho = ''
for pess in range (1,5):
    print('======{}ªpessoa========'.format(pess))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    s += idade 
    if (sexo == 'F'):
        if (idade < 20):
            mulher += 1
    if (sexo == 'M') and (idade > maior):
        maior = idade
        nomevelho = nome
media = s /4 
print('A media de idade do grupo é de {:.2f} anos'.format(media))
print('A quantidade de mulheres com menod de 20 anos lida foi de {}'.format(mulher))
print('O Homem mais velho tem {} anos e se chama {}'.format(maior, nomevelho))

