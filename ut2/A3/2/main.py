import math

num = int(input('Introduce un número:'))
result = 0

if num < 0:
    print('El número debe ser positivo')
else:
    for value in range (1, num + 1):
        result += value ** 2
    print(result)