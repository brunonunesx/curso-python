from random import randint
from time import sleep
print('\033[33m-=\033[m'*27)
print('\033[34mVou pensar em número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=\033[m'*27)
n = int(input('Escolha um número entre 0 e 5? '))
computador = randint(0, 5) #faz o computador sotear um numero de 0 a 5
print('PROCESSANDO...')
sleep(2)
if (n == computador):
    print('\033[31mVc acertou\033[m')
else:
    print('\033[31mVc errou\033[m')
print('Eu pensei no número {}'.format(computador))
