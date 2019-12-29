# try:
# 	articulos = int(input('Articulos: '))
# 	precio = int(input('Precio: '))
# 	print(f'Pagar: {str(articulos*precio)}€')
# except Exception as e:
# 	print('error! Deben ser numeros')

import datetime

while True:
	try:
		fecha = input('Introducir fecha dd-mm-aaaa: ')
		fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y')
		break

	except:
		print('Fecha incorrecta\n')

print(fecha)