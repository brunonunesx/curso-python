maior = 0 
menor = 0 
for p in range(0,5):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if (p == 0):
        maior = peso 
        menor = peso 
    else:
        if peso > maior:
            maior = peso 
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))