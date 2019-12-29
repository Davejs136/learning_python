# /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Declaraciones de variables

numero_entero = 5
n = y = z = 5    # Asignacion multiple: n = 5, y = 5, z = 5
m, n = 5, 4 * 8  # Asignacion multiple: m = 5 y n = 32
p1, p2 = (1,2)   # Asignacion multiple de tupla: p1 = 1 y p2 = 2

cadena = 'Python3' # Declara cadena alfanumerica
cadena = 'Pytonisos\tdel\tmundo\n' # incluye tab y salto de linea
cadena = '''Cadenas
			que ocupan
			varias lineas'''

num_float = 23.45  # numeros con decimales
num_float = 0.1e-3 # numeros con notacion cientifica
num_hexad = 0x23   # numeros hexadecimal

boolean = False
boolean = True
boolean_negar = not boolean # value: True output: false
numero_complejo = 4 + 3j * 2 # (4+6j)

cadena1 = '2.5'
cadena2 = '5'
numero1 = float(cadena1) # convierte en valor float
numero2 = int(cadena2)   # convierte en valor integer

# Operaciones con variables
cadena1 = 'Python'
cadena2 = cadena1.upper() # PYTHON
cadena3 = cadena1.lower() # python
cadena4 = cadena3 * 2     # pythonpython
print(type(cadena1))      # imprime el tipo de dato
del cadena1 			  # borra la variable de la memoria
print(cadena1)            # da error porque la variable ya no existe

# ord() chr()
ord('$')  # 36
chr(36)   # $

# Metodos para evaluar cadenas
cadena1 = 'Cuba'
cadena2 = 'Costa Rica'
print(cadena.isalpha()) # True
print(cadena.isalnum()) # True
print(cadena.isdecimal()) # False
print(cadena.isspace()) # False
print(cadena.istitle()) # True
if cadena1.isalpha():
	print('Todos los caracteres que contiene son alfanumericos')