velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print('\033[31mMULTADO, vc foi multado, o valor da multa é {}\033[m'.format(multa))
else:
    print('\033[32mParabéns vc esta dentro do limite continue assim\33[m')
