# !/usr/bin/python3

class Alumno:
	''' Clase para alumnos '''
	num_alumnos = 0
	sum_notas   = 0

	def __init__(self, nombre, nota):
		self.nombre = nombre
		self.nota = nota
		Alumno.num_alumnos += 1
		Alumno.sum_notas += notas

	def mostrarNombreNota(self):
		return(self.nombre, self.nota)

	def mostrarNumAlumnos(self):
		return(Alumno.num_alumnos)

	def mostrarSumNotas(self):
		return(Alumno.sum_notas)

	def mostrarNotaMedia(self):
		if Alumno.num_alumnos > 0:
			return(Alumno.sum_notas / Alumno.num_alumnos)
		else:
			return('Sin Alumnos')

alumno1 = Alumno('Maria', 8)
alumno2 = Alumno('Carlos', 6)