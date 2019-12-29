# /usr/bin/python3
# -*- coding: utf-8 -*-

# try:
# 	numero = int(input('Introducir un numero: '))
# 	factorial = 1
# 	for num in range(1, numero+1):
# 		factorial *= num

# 	print(factorial) 

# except:
# 	print('Debe introducir un numero entero')

try: # BLoque a vigilar
	texto = input('Teclear: ') # Introducir un dato

except KeyboardInterrupt: # Captura de excepcion de interrupcion
	print('\nSe ha pulsado ctrl+c') # interrupcion al presionar

else: # Se ejecuta si no hay error
	print(f'Ha tecleado {texto}') #muestra texto introducido

finally:
	print('Fin del programa') # muestra mensaje final


""" Con El generador de Exceopciones """

class LongPass(Exception):
	""" Excepcion definida por usuario """
	def __init__(self, longitud):
		Exception.__init__(self)
		self.longitud = longitud

try:
	clave = input('Digite contraseña')
	if len(clave) < 6:
		raise LongPass(len(clave)) # Llama a excepcion de usuario

except LongPass as lp:
	print(f'LonPass: Error por longitud {lp}')

else:
	print('No hubo error')