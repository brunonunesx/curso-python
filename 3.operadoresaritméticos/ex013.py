sal = float(input('Qual o sálario do funcionário '))
saln = sal + (sal * 15/100)
print('o salário do funcionário antigo é de R${}, novo salário do funcionário é R${:.2}'.format(sal, saln))