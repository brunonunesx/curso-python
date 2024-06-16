print ('-='*15)
print('Analisando um triângulo')
print ('-='*15)
seg1 = int(input('Digite um número para o primeiro segmento do triângulo '))
seg2 = int(input('Digite um número para o segundo segmento do triângulo '))
seg3 = int(input('Digite um número para o terceiro segmento do triângulo '))

if (seg1+seg2 > seg3) and (seg1 + seg3 > seg2) and (seg3 + seg2 > seg1):
    print('Os três segmento formam um triângulo',end='')
    if (seg1 == seg2) and (seg1 == seg3):
        print('O triângulo é equilátero')
    elif(seg1 != seg3) and (seg1 != seg2) and (seg2 != seg3):
        print('o triângulo é escaleno')
    else:
        print('O triângulo é isóceles')
else:
    print('três segmento não formam um triângulo')