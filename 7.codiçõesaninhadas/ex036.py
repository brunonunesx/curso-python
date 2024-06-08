valor = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
ano = int(input('Em quantos anos deseja pagar: '))

p = valor/(ano * 12) 
minimo = sal * 30 / 100 

print('Para pagar uma casa de R${:.2f} em {} anos \na prestação será de R${:.2f}'.format(valor, ano, p))


if (p > minimo):
    print('O emprestimo foi negado')
else: 
    print('O emprestimo foi aceito')
