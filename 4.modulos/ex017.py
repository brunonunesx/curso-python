'''Equação para triângulo retângulo
    a² + b² = h²'''
from math import sqrt
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
hip = sqrt((cato ** 2 ) + (cata ** 2))  
print('O valor da hipotenusa é {:.2f}'.format(hip))