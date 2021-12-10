
cantidad = int(input("ingrese una cantidad "))

if cantidad <= 0:
    print ("La cantidad que ha introducido no se puede cambiar")

if cantidad >= 50:
    unidades = cantidad // 50
    print (str(unidades) + " billetes de 50 euros")
    cantidad = cantidad % 50

if cantidad >= 20:
    unidades = cantidad // 20
    print (str(unidades) + " billetes de 20 euros")
    cantidad = cantidad % 20

if cantidad >= 10:
    unidades = cantidad // 10
    print (str(unidades) + " billetes de 10 euros")
    cantidad = cantidad % 10

if cantidad >= 5:
    unidades = cantidad // 5
    print (str(unidades) + " billetes de 5 euros")
    cantidad = cantidad % 5

if cantidad >= 2:
    unidades = cantidad // 2
    print (str(unidades) + " monedas de 2 euros")
    cantidad = cantidad % 2

if cantidad >= 1:
    unidades = cantidad // 1
    print (str(unidades) + " monedas de 1 euros")
    cantidad = cantidad % 1

