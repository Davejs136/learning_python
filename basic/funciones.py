# /usr/bin/python3
# -*- encoding: utf-8 -*-

def area_triangulo(base, altura):
	''' Calcular el area de un triangulo '''
	return base * altura / 2

# funciones con numeros de variables indefinidos
def distancia(*tramos):
	''' Suma la distancia entre tramos '''
	total = 0
	for distancia in tramos:
		total += distancia
	return total # Devuelve la suma de todos los tramos

tramo1 = 10
# print(distancia(tramo1, 20, 30, 40)) # Devolvera 100
# print(distancia()) # Devolvera 0

# Funciones con parametros con valores por defectos
def pagar(importe, dto_aplicado = 5):
	''' La funcion aplica descuentos '''
	return importe - (importe * dto_aplicado / 100)

# print(pagar(1000)) # 950
# print(pagar(1000, 10)) # 900

# Funciones que se les pasa los valores por palabras clave
def repite_caracter(caracter='-', repite=3):
	return caracter * repite

# print(repite_caracter())
# print(repite_caracter('.', 10))
# print(repite_caracter(repite=5, caracter='*'))

# funciones con parametros que contienen diccionarios
def porc_aprobados(aprobados, **aulas):
	''' Calcula el % de aprobados '''

	total = 0
	for alumnos in aulas.values():
		total += alumnos

	return aprobados * 100 / total

porcentaje_aprobados = porc_aprobados(48, A=22,B=25,C=21)
# print(porcentaje_aprobados) 

# Funciones que devuelven mas de un valor
def elemento_quimico(simbolo):
	''' Devuelve numero atomico y denominacion del elemento '''

	elementos = {
		'H': '1-Hidrogeno',
		'He': '2-Helio',
		'Li': '3-Litio'
	}

	elemento = elementos[simbolo]
	lista = elemento.split('-')

	return (lista[0], lista[1])

num_atomico, denomina = elemento_quimico('He')
# print('Num. Atomico: ', num_atomico)
# print('Denominacion: ', denomina)

# Funciones sin return
# Estas por lo general se utilizan para imprimir
# si es asignada a una variable devolvera None

def repite(caracter='-', repite=3):
	print(caracter * repite)

#repite('=', 20)