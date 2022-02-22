imput_num = input('Introduce un número:')
quantity_num = len(imput_num)
num_summary = 0

for i in imput_num:
    i = float(i)
    num_summary += i
result = num_summary / quantity_num
print(f"La media es: {result}")