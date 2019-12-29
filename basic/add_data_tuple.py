# /usr/bin/python3
# -*- coding: utf-8 -*-

users_default = ('Daniel', 'Josue', 'Stiven')

while True:
	user = input('Ingrese su usuario: ')

	for x in users_default:
		if x == user:
			print(f'Bienvenid@ {user}')
	break