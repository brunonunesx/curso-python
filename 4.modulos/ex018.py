'''seno conseno e tangente'''
import math
num = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(num))
cons = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O seno é {:.2f} \nO conseno é {:.2f}\nA tangente é {:.2f}'.format(sen, cons, tan))
