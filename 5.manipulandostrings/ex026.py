frase = str(input('digite uma frase')).upper().strip()
print('A frase {} tem {} letras A '.format(frase, frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
