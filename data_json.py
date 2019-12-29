import json

"""
	json package
	Es una libreria o paquete de python con el que se puede
	manejar objetos json(Javascript Object Notation).
	+ json.dumps() y json.dump() serializa el objeto a un archivo
	  de texto.
	+ json.load() lee el archivo codificado (decodifica)
"""

var_json = json.dumps([1, 'Simple', 'lista'])

print(type(var_json))