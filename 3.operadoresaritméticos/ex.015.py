km = float(input('Qual foi a quatidade de km pecorridos? '))
dias = int(input('Qual foi a quatidade de dias utilizados? '))
valor = (60 * dias) + (0.15 * km)
print('O preço a se pagar é de {:.2f}'.format(valor))