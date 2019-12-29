''' 
	Hacer un programa que me permita saber si un
	numero es mayor, menor o igual a 0
'''

# for x in range(5):
# 	num = int(input('Digite un valor: '))

# 	if num < 0:
# 		print('El numero es negativo')
# 	elif num > 0:
# 		print(f'El numero {num} es positivo')
# 	else:
# 		print('Ambos numeros son iguales')

'''
	Hacer que el usuario compre boletos de avion
	ejecutivo: 50
	medio: 150
	economico: 100
'''

"""medio = 150 
ejecutivo = 50
economico = 100

for x in range(300):
	if economico == 0 and medio == 0 and ejecutivo == 0:
		print('No quedan boletos')
		break

	print(f'''\t\t     *** Tipos de boletos ***
			 * 1 economico: {economico} 
			 * 2 medio: {medio}
			 * 3 ejecutivo: {ejecutivo}
			 * 5 Exit
		     *************************\n''')

	tipo = int(input('Ingrese el tipo de boleto: '))

	if tipo == 1:
		cantidad = int(input('Ingrese la cantidad de boletos economicos: '))
		if cantidad > economico:
			print('Limite de boletos excedidos')
		else:
			economico -= cantidad
			print(f'Ud ha comprado: {cantidad} de boletos')
	elif tipo == 2:
		cantidad = int(input('ingrese la cantidad de boletos medios: '))
		if cantidad > medio:
			print('Limite de boletos excedidos')
		else:
			medio -= medio
			print(f'Ud ha comprado: {cantidad} de boletos')
	elif tipo == 3:
		cantidad = int(input('ingrese la cantidad de boletos ejecutivos: '))
		if cantidad > ejecutivo:
			print('Limite de boletos excedidos')
		else:
			ejecutivo -= ejecutivo
			print(f'Ud ha comprado: {cantidad} de boletos')
	elif tipo == 5:
		print('Gracias por su visita')
		break
	else:
		print(f'Opcion {tipo} no es valido') """


# Tickes Airplane POO

class Ticket():
	""" Class to buy airplanes tickets """
	def __init__(self, ejecutive, middle, economic):
		self.ejecutive = ejecutive
		self.economic = economic
		self.middle = middle

	def run(self):
		option = self.cin('Enter option: ')
		while True:
			# Economic
			if option == 1:
				self.cant_tickets(self.economic)
				self.run()
			# Middle
			elif option == 2:
				self.cant_tickets(self.middle)
				self.run()
			# Ejecutive
			elif option == 3:
				self.cant_tickets(self.ejecutive)
				self.run()
			# Show status
			elif option == 4:
				self.status()
				self.run()
			# Exit
			if option == 0:
				print('Script finish!')
				break

	def cant_tickets(self, ticket_type):
		tickets = self.cin(f'Enter the mount tickets {ticket_type}: ')
		if tickets > ticket_type:
			print('Limit ticktes')
		else:
			ticket_type -= tickets
			print(f'You are buy {tickets} tickets')

	def cin(self, string):
		return int(input(string))

	def status(self):
		print(f'''\t\t     *** Tipos de boletos ***
			* 1 economico: {self.economic} 
			* 2 medio: {self.middle}
			* 3 ejecutivo: {self.ejecutive}
			* 4 status
			* 5 Exit
			*************************\n''')

ticket = Ticket(50, 150, 100)
ticket.run()