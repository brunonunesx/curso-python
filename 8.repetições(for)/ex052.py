num = int(input('Digite um número: '))
tot = 0
for c in range (1, num+1):
    if(num % c == 0 ):
        tot += 1
    print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes'.format(num, tot))
if (tot == 2):
    print('{} Esse número é primo'.format(num))
else:
    print('{} Esse número não é primo'.format(num))

