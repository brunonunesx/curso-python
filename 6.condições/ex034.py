salario = float(input('Qual o salário de um funcionário '))
if (salario > 1250):
    salario = salario + (salario * 10 / 100)
else:
    salario = salario + (salario * 15 / 100)
print('Seu aumento foi de {:.2f}'.format(salario))
