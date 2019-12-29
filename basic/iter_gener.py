# /usr/bin/python3
# -*- encoding: utf-8 -*-

# recorrer los caracteres de una cadena

cadena = 'Python'
for char in cadena:
	pass # print(char)

# Recorrer carateres de una cadena en sentido inverso

for char in cadena[::-1]:
	pass # print(char)

# Recorrer los elementos de una lista

lista = ['una', 'lista', 'es', 'un', 'iterable']
for word in lista:
	pass # print(word)

# Recorrer los elementos de una lista en sentido inverso

for word in lista[::-1]:
	pass # print(word)

# Obtener indice para recorrer todos los elementos de la lista

for indice in range(len(lista)):
	pass # print(indice, lista[indice])

# Recorrer las claves de un diccionario

artistas = {'Lorca': 'Escritor', 'Goya': 'Pintor'}
for clave, valor in artistas.items():
	pass # print(clave, ': ', valor)

# Leer las lineas de un archivo de texto, una a una

for linea in open("datos.txt"):
	pass # print(linea.rstrip())

lista = [10, 100, 1000, 100000]
iterador = iter(lista)

# try:
# 	while True:
# 		print(iterador.__next__())
# except StopIteration:
# 	print('Se ha alcanzado el final de la lista')

# Declara clase para recorres caracteres de cadena de texto
# desde el ultimo al primer caracter

class Invertir:
	def __init__(self, cadena):
		self.cadena = cadena
		self.puntero = len(cadena)

	def __iter__(self):
		return(self)

	def __next__(self):
		if self.puntero == 0:
			raise(StopIteration)
		self.puntero = self.puntero - 1
		return(self.cadena[self.puntero])

# Declara iterable y recorre caracteres

cadena_invertida = Invertir('Iterable')
iter(cadena_invertida)

for char in cadena_invertida:
	pass # print(char, end=' ')

# Devuelven caracteres que restan por iterar (ninguno):

# print(len(cadena_invertida.__iter__())) # []

# Declara generador

def gen_basico():
	yield "uno"
	yield "dos"
	yield "tres"

for valor in gen_basico():
	pass# print(valor)

# Crea objeto generador y muestra tipo de objeto

generador = gen_basico()
# print(generador)
# print(type(generador))

# Convierte a lista el objeto generador y muestra elementos

lista = list(generador)
# print(lista)
# print(type(lista))

def gen_diez_numeros(inicio):
	fin = inicio + 10
	while inicio < fin:
		inicio+=1
		yield inicio, fin

for inicio, fin in gen_diez_numeros(23):
	pass # print(inicio, fin)

def get_info():
	yield 'name: Dave'
	yield 'age: Nineteen years old'

info = get_info()

print(info.__next__())
print('last info')
print(info.__next__())