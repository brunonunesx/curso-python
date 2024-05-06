distancia = float(input('Qual foi a distancia da viagem KM?'))
if (distancia <= 200):
    preço = distancia * 0.5
else:
    preço= distancia * 0.45
print('O valor para a viagem de {}KM foi de {}'.format(distancia, preço))