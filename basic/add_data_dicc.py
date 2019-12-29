# /usr/bin/python3
# -*- coding: utf-8 -*-

users = {}

while True:
	print('** Bienvenido a mi Script **')
	print('1 ---> Ingresar al sistema')
	print('2 ---> Registrarse')
	print('3 ---> Salir del Script')

	option = int(input('> '))

	if option == 1:
		if not users:
			print('No existe ningun usuario!')
		else:
			try:
				user = input('Ingrese su usuario: ')
				passwd = int(input('Ingrese contraseña: '))
			except ValueError:
				print('Dato no admitido')

	if option == 2:
		try:
			new_user = input('Ingrese el nombre de su usuario: ')
			new_passwd = int(input('Ingrese contraseña (solo digitos): '))
			users[new_user] = new_passwd
		except ValueError:
			print('Dato no admitido')

	if option == 3:
		break