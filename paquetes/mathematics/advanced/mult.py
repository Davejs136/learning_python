"""
	. ---> Busca al mismo nivel
	.. --> Sube un nivel y encuentra el modulo requerido
"""

from ..superior import Superior

class Multiplication(Superior):
	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2