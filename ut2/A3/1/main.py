import math

print('Introduce un número')
num = int(input())

if num <= 0:
    print('El programa solo admite numeros positivos.')
else:
    for value in range(2, num):
        if num % value == 0:
            print('Este no es un numero primo.')
            break
    else:
        print ('Este es un numero primo.')