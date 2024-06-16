valor = float(input('Qual o valor do produto: (R$)'))
pag = int(input('forma de pagamento \n[1] à vista \n[2] à vista no cartão \n[3] 2x no cartão \n[4] 3x no cartão o mais \nQual é a opção? '))

if (pag == 1):
    des =  valor - valor * 10 /100
    print('O valor a se pago é {:.2f}R$'.format(des))
elif (pag == 2):
    des = valor - valor * 5 /100 
    print('O valor a se pago é {:.2f}R$'.format(des))
elif (pag == 3): 
    parcela = valor / 2
    print('O valor a se pago é de {:.2f}R$ sua compra parcelada em 2x ficou em {:.2f}R$'.format(valor, parcela))
elif (pag == 4):
    parcela = (valor + (valor * 20 / 100))
    vezes = int(input('Em quantas vezes vai quere parcelar? '))
    total = parcela/vezes
    print('O valor a se pago é de {:.2f}R$ parcelado em {}vezes'.format(total,vezes))
else:
    print('Opçao inválida de pagamento')
