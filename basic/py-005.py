# /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Evaluar distintos valores numericos
if edad <= 12:
	precio = 2
elif 13 <= edad <= 18:
	precio = 3
else:
	precio = 4
print(f"A pagar: {str(precio)}$")


# Evaluar en una sola linea
print('par' if edad % 2 == 0 else 'impar')

# Evaluar si un valor esta entre varias opciones
tecla = 'S'

if tecla in('s','S','y','Y'):
	print('Ha seleccionado Si')

# Evaluar si cadena, lista o diccionario estan vacios
var1 = ''
var2 = []
var3 = {}

if not var1:
	print('Cadena Vacia')

if not var2:
	print('Lista sin elementos')

if not var3:
	print('Diccionario vacio')

# Evaluar si una variable no tiene ningun valor
var4 = None

if not var4:
	print('No tiene valor')



""" Ciclos """

# Ciclo While
contador = 0
limite = 5

while contador < 11:  # El bucle terminar cuando contador = 10
	if contador == limite:
		break
	else:
		contador += 1
		print(contador, limite)

# Ejemplo de bucle con 'continue' and 'break'
x = 0
y = 0
limite = 5

while True:
	y+=1
	if y!= limite:
		x+y
	else:
		break
	if y!=3:
		continue
	print(x,y)

# Ciclo for..in
num_win = [1,2,3,4,5,6,7,8,9]
for num in num_win:
	if num == 9:
		print(f'Ha ganado el numero: {num}')
		break

for num in range(10):
	print(num) # recorre del 0 al 9