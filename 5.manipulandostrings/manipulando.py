frase = 'Curso em Video Python'
'''Fatiamento'''
print(frase[4])
print(frase[:21])

'''Análise'''
len(frase)
frase.count('o', 0, 14)
frase.find('deo')
'curso' in frase

'''Transformação'''
frase.replace('Python','Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
frase.strip()
frase.rstrip()
frase.lstrip()

'''Divisão'''
frase.split()
'-'.join(frase)
