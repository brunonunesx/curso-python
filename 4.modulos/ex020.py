from random import shuffle
au1 = str(input('Qual o nome do primeiro aluno? '))
au2 = str(input('Qual o nome do segundo  aluno? '))
au3 = str(input('Qual o nome do terceiro aluno? '))
au4 = str(input('Qual o nome do quarto aluno? '))
lista = [au1, au2, au3, au4]
shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))
