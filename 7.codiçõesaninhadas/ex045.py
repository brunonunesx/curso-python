from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

jogador= int(input('''Escolha sua jogada
[0] Pedra
[1] Papel
[2] Tesoura
Qual é sua jogada?'''))
computador = randint(0,2)

print('jo')
sleep(1)
print('ken')
sleep(1)
print('po!!!')

print('-='*11)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-='*11)

if computador == 0:
    if jogador == 0: 
        print('empate')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('jogador perdeu')
    else:
        print('opção inválida')         
elif computador == 1:
    if jogador == 0: 
        print('jogador perdeu')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('opção inválida')      
elif computador == 2:
    if jogador == 0: 
        print('jogador venceu')
    elif jogador == 1:
        print('jogador perdeu')
    elif jogador == 2:
        print('empate')
    else:
        print('opção inválida')      


