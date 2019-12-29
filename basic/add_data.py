# /usr/bin/python3
# -*- coding: utf-8 -*-

shopping_list = []

name  = input('Ingrese su nombre: ')
gender = input('Ingrese sexo(m|f): ')

while True:
	# Verifico el genero para la presentacion
	if gender == 'm':
		print(f'\n** Bienvenido {name} **\n')
	else:
		print(f'** Bienvenida {name} **\n')

	# Input Interactivo
	option = input('Ingrese una opcion ("h" para ayuda): ')

	# Agregar nuevo elemento
	if option == '1':
		new_element = input('Ingrese nuevo elemento: ')
		shopping_list.append(new_element)

	# Buscar elemento
	elif option == '2':
		search_element = input('Ingrese el elemento a buscar: ')
		try:
			index = shopping_list.index(search_element)
			print(index)
		except ValueError:
			print(f'"{search_element}" no existe')
			continue

	# Eliminar un elemento
	elif option == '3':
		element_to_delete = input('Ingrese el nombre del elemento: ')
		try:
			index = shopping_list.index(element_to_delete)
			shopping_list.pop(index)
			print(f'El elemento "{element_to_delete}" fue eliminado')
		except ValueError:
			print(f'{element_to_delete} no existe')
			continue

	# Ver lista
	elif option == '4':
		print(shopping_list)

	# Borrar toda la lista
	elif option == '5':
		shopping_list[:] = []
		print('Se borro toda la lista...')

	# Mostrar ayuda
	elif option == 'h':
		print('** Las opciones son las siguientes: **')
		print('1 -> para añadir elementos a lista de compras')
		print('2 -> para buscar elementos de la lista de compras')
		print('3 -> para eliminar un elemento')
		print('4 -> para ver la lista')
		print('5 -> Eliminar toda la lista\n')

	else:
		print(f'Opcion "{option}" no valida\n')
		continue