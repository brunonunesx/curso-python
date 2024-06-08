s = 0 
for c in range (0,2):
    n = float(input('Digite a nota do aluno: '))
    s = s + n

m = s / 2
print('A média do aluno foi de {} pontos'.format(m))

if(m <= 5):
    print('O aluno foi reprovado')
elif(m > 5) and (m <= 7):
    print('O aluno está de recuperação')
else:
    print('O aluno está Aprovado')
