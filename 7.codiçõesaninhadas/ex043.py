peso = float(input('Qual é seu peso ?  (Kg)'))
altura = float(input('Qual é sua altura?  (m)'))

imc = peso / altura**2

print('Seu indice de massa corporal é de {:.2f}'.format(imc))

if (imc <= 18.5):
    print('Abaixo do peso')
elif(imc <= 25 ):
    print('Peso ideal')
elif (imc <= 30 ):
    print('Sobrepeso')
elif (imc <= 40):
    print('Obesidade')
else:
    print('Obesidade mórbida')