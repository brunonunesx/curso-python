print('-='*13)
print('Soma de números ímpares')
print('-='*13)

s = 0
cont = 0
for c in range (1, 501, 2):
    if (c % 3 == 0):
        print(c)
        s = s + c
        cont  = cont + 1
print('A soma dos números ímpares e divisivéis por 3 é {} o total de números somados é {}'.format(s,cont))