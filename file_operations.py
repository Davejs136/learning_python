# !/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
### open(ubicacionYnombre, modo(lectura|escritura|etc), codificacion)
	- Si no se indica el tipo de operacion, el archivo se abrira en modo
	  lectura
	- Si se omite la decodificacion se utilizara la codificacion del sistema
	- Si no existe la ruta producira una excepcion del tipo IOerror
"""
location = '/home/david/Desktop/dev/python/learning_python/learning_python/sample.txt'

file = open(location)
file = open(location, 'r')
file = open(location, mode='r', encoding='utf-8')

# Que codificacion utiliza nuestro sistema ?
# import locale
# print(locale.getpreferredencoding()) # UTF-8

"""
	Las operaciones que pueden realizarse sobre un archivo:
	r   ------> Lectura
	r+  ------> Lectura/Escritura
	w   ------> Sobreescritura. Si no existe se creará
	a   ------> Añadir. Escribe al final del archivo
	b   ------> Binario
	+   ------> Permite lectura/escritura simultánea
	U   ------> Salto de linea universal: win cr+if, linux lf y mac cr
	rb  ------> Lectura binaria
	wb  ------> Sobreescritura Binaria
	r+b ------> Lectura/Escritura binaria
"""

# Despues de terminar de trabajar con un archivo
# Se cierra con el metodo close()

"""
Leer archivo: read, readline, readlines, with-as

	read(): es posible leer un número de bytes determinados. 
		Si no se indica número se leerá todo lo que reste o 
		si se alcanzó el final de fichero devolverá una cadena vacía.

	readline(): Lee de un archivo una linea completa

"""

### Read()

# Abre el archivo en modo lectura
file = open('./sample.txt', 'r')

# Lee los 9 primeros bytes
cadena1 = file.read(9)

# print(cadena1)

# Lee la informacion que reste
cadena2 = file.read()

# print(cadena2)

# Cierra el archivo
file.close()

### Readlines()
file = open('./sample.txt', 'r')

# Inicia un bucle infinito para leer linea a linea
while True:
	linea = file.readline() # lee linea
	if not linea:
		break # Si no hay mas se rompe el bucle
	#print(linea) # Muestra la linea leida

file.close()


# El método readlines() lee todas las líneas de un archivo como una lista. 
# Si se indica el parámetro de tamaño leerá esa cantidad de 
# bytes del archivo y lo necesario hasta completar la última linea.
file = open('./sample.txt', 'r')

# lee todas las lineas y asigna a lista
lista = file.readlines()

# Inicializa un contador
numlin = 0

# Recorre todos los elementos de la lista
for linea in lista:
	# Incrementa en 1 el contador
	numlin += 1

	# Muestra contador y elemento (linea)
	# print(numlin, linea)

file.close()

### with-as: Permite usar los archivos de forma optima
# cerrandolos y liberando la memoria al concluir el proceso de lectura

# Abre archivo (y cierra cuando termine lectura)
with open('./sample.txt') as file:
	# recorre linea a linea el archivo
	for linea in file:
		# Muestra linea ultima leida
		pass # print(linea)

"""
Escribir en archivo: write, writelines

	write(): Escribe una cadena

	writelines(): Escribe una lista a un archivo

	- Si no existe el archivo, se crea uno nuevo
"""

cadena1 = 'Datos' # declara cadena1
cadena2 = 'Secretos' # Declara cadena2

# Abre archivo para escribir
file = open('./datos.txt', 'w')

# Escribe cadena1 añadiendo salto de linea
file.write(cadena1 + '\n')

# Escribe cadena2 en archivo
file.write(cadena2)
file.close()

with open('./datos.txt') as data:
	for linea in data:
		pass # print(linea)

# Declara lista
lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

# Abre archivo en modo escritura
file = open('./datos.txt', 'w')

# Escribe toda la lista en el archivo
file.writelines(lista)
file.close()

with open('./datos.txt') as data:
	for linea in data:
		pass # print(linea)

"""
Mover el puntero: seek, tell
	
	seek(): Desplaza el puntero a una posicion del archivo

	tell(): devuelve la posicion del puntero en un momento dado (en bytes)
"""

# Abre en modo lectura
file = open('./sample.txt')

# Mueve el puntero al quinto byte
file.seek(5)

# Lee los siguientes 5 bytes
cadena1 = file.read(5)

# Muestra cadena
# print(cadena1)

# Muestra la posicion del puntero
# print(file.tell())

file.close()

"""
Leer y escribir cualquier objeto a un archivo

	Para leer y escribir cualquier tipo de objeto 
	Python podemos importar el modulo pickle y usar 
	sus métodos dump() y load() para leer y escribir los datos.
"""

# Importar modulo pickle
from pickle import dump, load

# Declarar lista
lista = ['Perl', 'Python', 'Javascript']

# Abre archivo binario para escribir
file = open('./lenguajes.dat', 'wb')

# Escribe la lista en archivo
dump(lista, file)

file.close()

# Borra de memoria la lista
del lista

# Abre archivo binario para leer
file = open('./lenguajes.dat', 'rb')

# Carga lista desde archivo
lista = load(file)

# Muestra lista
print(lista)

# Cierra archivo
file.close()