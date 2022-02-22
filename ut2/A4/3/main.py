input_num = int(input('input_num:'))
chain = input('chain:')
word, count = 0, 0
chain = chain + ' '

if input_num <= 0:
    print('Introduzca un número positivo')
else:
    for char in chain:
        if char != ' ':
            count += 1
        else:
            if count == input_num:
                word += 1
                count = 0
            else:
                count = 0

print(f'Hay {word} palabras de tamaño {input_num}')