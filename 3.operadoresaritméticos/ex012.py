produto = float(input('Qual o preço do produto? '))
p = produto - (produto * 5/100)
print('O produto de valor {}R$ com o desconto de 5% f1icara {:.2f}R$'.format(produto, p))