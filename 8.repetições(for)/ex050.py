s = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if (num % 2 == 0):
        cont += 1
        s += num
print('A soma dos números pares digitados é {} você informou {} números pares'.format(s,cont))