num = int(input('num:'))

if num <= 0:
    print('Escriba un número positivo.')
else:
    for i in range(1, num + 1):
        result = 1
        for k in range (i, 0, -1):
            result *= k
        print (i,'! =', result)