# !/usr/bin/python3
# -*- encoding: utf-8 -*-

from math import pi

# Para la funcion reduce
from functools import reduce

""" 
	El siguiente ejemplo construye un conversor de 
	números anidando varias funciones en una función 
	de orden superior. 
"""


def conversor(sis):
	def sis_bin(numero):
		print(f'dec: {numero}, bin: {bin(numero)}')

	def sis_oct(numero):
		print(f'dec: {numero}, oct: {oct(numero)}')

	def sis_hex(numero):
		print(f'dec: {numero}, hex: {hex(numero)}')

	sis_func = {'bin': sis_bin, 'oct': sis_oct, 'hex': sis_hex}
	return sis_func[sis]

# Crea una instancia del conversor hexadecimal
conversor_hex = conversor('hex')

# Convierte 100 de decimal a hexadecimal
conversor_hex(100)

# Otro modo de usar el conversor
# Convierte 9 de decimal a binario
conversor('bin')(9)


# Funciones de orden superior:

# Funcion map()
#  Aplica una función a una lista de datos y 
# 	devuelve un iterador que contiene todos los 
# 	resultados para los elementos de la lista.

def cuadrado(num):
	return num ** 2

lista1 = [-2, 4, -6, 8]

# Convierte a lista el iterador obtenido
lista2 = list(map(cuadrado, lista1))

# Muestra elementos de la lista
print(lista2) # 4, 16, 36, 64


def are_circulo(radio):
	return pi * radio ** 2

lista3 = [1, 2, 3]

# Devuelce iterador que es convertido a lista
lista4 = list(map(are_circulo, lista3))
print(f'area_circulo: {lista4}')

# Funcion filter()
# 	Aplica un filtro a una lista de datos y 
# 	devuelve un iterador con los elementos que superan el filtro.

# La funcion verifica si un numero es negativo
def es_negativo(num):
	# Devuelve True/False segun sea o no nro negativo
	return (num < 0)

lista5 = [-3, -2, 0, 1, 9, -5]

# Muestra los numeros negativos de la lista
# La funcion es_negativo() es llamada para comprobar,
# 	uno a uno, todos los numeros de la lista
print(f'Filter: {list(filter(es_negativo, lista5))}')

# Reduce una lista utilizando las condiciones pasadas
# por una funcion

def multiplicar(x, y):
	print(x * y) # Muestra el resultado parcial
	return x * y

lista = [1, 2, 3, 4]
valor = reduce(multiplicar, lista)
print(f'Reduce: {valor}') # Muestra valor final

# Lambda
# 	Se utiliza para declarar funciones que solo ocupan una 
# 	linea de codigo. Se pueden asignar a variables para usar luego

cuadro = lambda x: x*x

lista = [1,2,3,4,5,13]
for elemento in lista:
	pass# print(f'Lambda: {cuadrado(elemento)}')

# Lambda con 2 argumentos

area_triangulo = (lambda base,height: base * height / 2)
medidas = [(34, 8), (26, 8), (44, 18)]

for datos in medidas:
	base = datos[0]
	altura = datos[1]
	print(f'Lambda 2 args: {area_triangulo(base, altura)}')

""" Comprension de listas """
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cada elemento de la lista se eleva al cubo
cubos = [valor ** 3 for valor in lista]
print('Cubos de 1 a 10:', cubos)


numeros = [135, 154, 180, 193, 210]
divisiblespor3 = [valor for valor in numeros if valor % 3.0 == 0] 

# Muestra lista con los números divisibles por 3
print(divisiblespor3)  


# Define función devuelve el inverso de un número
def funcion(x):
    return 1/x

L = [1, 2, 3]  # declara lista

# Muestra lista con inversos de cada número
print([funcion(i) for i in L])

# Devuelve un conjunto (elementos no repetidos)
z = {elem for elem in [1, 2, 1, 2, 3, 1]}
print(z)  # {1, 2, 3}

# Devuelve un diccionario
dicc1 = {num: num**2 for num in range(1, 6)}
print(dicc1)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

""" Generadores """
# Define generador
def generador(inicio, fin, incremento):
	while(inicio <= fin):
		yield inicio # Devuelve valor
		inicio += incremento

# Recorre los valores del generador
for valor in generador(0, 6, 1):
	# Muestra los valores uno a uno
	print(valor) # 0 1 2 3 4 5 6

# Obtiene una lista del generador
lista = list(generador(0, 8, 2))

# Muestra la lista
print(lista) # [0, 2, 4, 6, 8]

""" La funcion Decorador """
# Es una función que recibe una función como parámetro 
# y devuelve otra función como valor de retorno

# Define decorador
def decorador1(funcion):
    # Define función decorada
    def funciondecorada(*param1, **param2):
        print('Inicio', funcion.__name__)
        funcion(*param1, **param2)
        print('Fin', funcion.__name__)
    return funciondecorada
    
def suma(a, b):
    print(a + b)

suma2 = decorador1(suma)
suma2(1,2)
suma3 = decorador1(suma)
suma3(2,2)

# Otra forma más elegante, usando @:

@decorador1
def producto(arg1, arg2):
    print(arg1 * arg2)

producto(5,5)


# El siguiente decorador genera tablas de sumas
# y multiplicaciones. El código que es común a todas 
# las funciones se declara en la función 'envoltura':

def tablas(funcion):
    def envoltura(tabla=1):
        print('Tabla del %i:' %tabla)
        print('-' * 15)
        for numero in range(0, 11):            
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura

@tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas
def multiplicar(numero, tabla=1):
    print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

# Muestra la tabla de sumar del 1
suma()

# Muestra la tabla de sumar del 4 
suma(4)

# Muestra la tabla de multiplicar del 1
multiplicar()

# Muestra la tabla de multiplicar del 10
multiplicar(10)  