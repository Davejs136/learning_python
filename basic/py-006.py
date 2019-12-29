# /usr/bin/python3
# -*- coding: utf-8 -*-

''' Listas, tuplas, diccionarios y conjuntos (set) '''

ListaEstaciones = ['Invierno', 'Primavera', 'Verano', 'Otoño']
lista = [] # Declaracion de lista vacia

TuplasDiasSemana = ('Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do')

# Operacion con cadenas y listas

cadena1 = 'Tengo una yama que Yama se llama'
lista1  = ['pera', 'manzana', 'naranja', 'uva']

longitud = len(cadena1)
elem_longitud = len(lista1) # 4, devuelve el nro de la lista
cuenta = cadena1.count('yama') # 1 sola aparicion de 'yama'
print(cadena1.find('yama')) # 10, devuelve posicion de busqueda

cadena2 = cadena1.join('***')
lista1  = cadena1.split(' ') # separa la cadena -> lista
tupla1  = cadena1.partition(' ') # separa la cadena por separador -> tupla
cadena2 = cadena1.replace('yama', 'cabra',1) # busca/sustituye terminos

numero = 3.14
cadena3 = str(numero) # convierte numero en cadena

if cadena1.startswith('tengo'): # evalua si comienza por 'tengo'
if cadena1.endswith('llama'): # Evalua si termina por 'llama'
if cadena1.find('llama') != -1: # Evalua si contiene 'llama'

cadena4 = 'Python'
print(cadena4[0:4]) # muestra desde la posicion 0 a 4: 'Pyth'
print(cadena4[1]) # Muestra la posicion 1: 'y'
print(cadena4[:3]+'-'+cadena4[3:]) # Muestra "Pyt-hon"
print(cadena4[:-3]) # Muestra todo menos las tres ultimas: 'Pyt'

# Operacion con Tuplas y Listas

lista1 = ['uno', 2, True]
lista2 = [1,2,3,4]
lista3 = ['nombre', ['one', 'two']]

print(lista2[0:3:1]) # [1,2,3], responde al patron inicio:fin:paso
print(lista[::-1]) # Devuelve la lista ordenada al reves

lista1.pop(0) # Borra elemento indicado o ultimo si no se indica
lista1.remove('uno') # Borra el primer elemento (por indice)
del lista[2] # Borra el tercer elemento (por indice)
lista1.append(7) # añade un elemento al final con append()
lista2.extend([9,1]) # Extiende la lista con otra al final
lista1.insert(1, 'dos') # Inserta nuevo elemento en posicion
del lista2[0:3] # Borra los elementos desde:ahora
lista[:] = [] # Borra todos los elementos de la lista
lista1.count(2) # cuenta el nro de veces que aparece 2
lista1.index('dos') # Busca posicion que ocupa elemento
lista3.sort() # Ordena la lista
lista3.sort(reverse=True) # Ordena la lista en orden inverso
lista5 = sorted(lista4) # Ordena lista destino

tupla1 = (1,2,3)
tupla2 = (10,) # Con un elemento terminar con ","
tupla3 = tuple([1,3,4]) # convierte lista en una tupla
tupla[0:3] # (1,2,3) accede a los valores desde:hasta

''' Diccionarios '''

# samples
capitales = {'Chile': 'Santiago', 'España': 'Madrid'}

print(f'La capital de España es {capitales['España']}')
del capitales['España'] # borra el par España:Madrid
len(capitales) # devuelve 1

for pais, capital in capitales.items():
	print(f'Capital de {pais} es {capital}')

capitales['Portugal'] = 'Lisboa'
if 'Portugal' in capitales: # Comprueba si existe clave
	print(f"La capital de Portugal es {capitales['Portugal']}")

# Operaciones con diccionarios
dic1 = {'Lorca': 'Escritor', 'Goya': 'Pintor'}

dic1['Lorca'] # Acceso a un valor por clave
dic1.get('Gala', 'no existe') # Acceso a un valor por clave

if 'Lorca' in dic1: print('esta') # comprueba si existe clave

dic1.items() # Obtiene una lista de tuplas clave:valor
dic1.keys() # Obtiene una lista de las claves
dic1.values() # Obtiene una lista de los valores

dic1['Lorca'] = 'Poeta' # añade un nuevo par clave:valor
dic1.update({'Carreras': 'Tenor'}) # añadir con update
del dic1['Amebar'] # Borra un par clave:valor
dic1.pop('Amebar', 'no esta') # borra par clave:valor

# Recorrer diccionarios con for...in
artistas = {'Lorca':'Escritor', 'Goya':'Pintor'} # diccionario
paises = ['Chile','España','Francia','Portugal'] # declara lista
capitales = ['Santiago','Madrid','París','Lisboa']  # declara lista
for c, v in artistas.items(): print(c,':',v)  # recorre diccionario
for i, c in enumerate(paises): print(i,':',c)  # recorre lista 
for p, c in zip(paises, capitales): print(c,' ',p) # recorre listas
for p in reversed(paises): print(p,)  # recorre en orden inverso
for c in sorted(paises): print(c,)  # recorre secuencia ordenada

# Recorrer rangos con for...in range()
for num in range(7): print(num)  # recorre de 0 a 6
for num in range(1,8): print(num)  # recorre de 1 a 7
for num in range(10,50,5): print(num) # de 10 a 45 de 5 en 5
for num in range(0,-10,-1): print(num)  # de 0 a -9 de -1 en -1

lista = ["Chorizo","Jamón","Morcilla","Salchichón"]  # lista
for elemento in range(len(lista)):  # recorre elementos de lista
    print (elemento, lista[elemento])  # muestra posición y elemento

# Operadores de secuencia: in, not in, is, is not
cadena = 'Python'  # asigna cadena a variable
lista = [1, 2, 3, 4, 5]  # declara lista
if 'y' in cadena: print('“y” está en “Python”')  # contiene
if 6 not in lista: print('6 no está en la lista') # no contiene
if 'abcabc' is 'abc' * 2: print('Son iguales')  # son iguales

''' Conjuntos Set '''
# - diferencia, | unión, & intersección y ^ diferencia simétrica

conjunto = set()  # Define un conjunto vacío
lista = ['vino', 'cerveza', 'agua', 'vino']  # define lista
bebidas = set(lista)  # define conjunto a partir de una lista
print('vino' in bebidas)  # True, 'vino' está en el conjunto
print('anis' in bebidas)  # False, 'anis' no está en el conjunto
print(bebidas)  # imprime {'agua', 'cerveza', 'vino'}
bebidas2 = bebidas.copy()  # crea nuevo conjunto a partir de copia
print(bebidas2)  # imprime {'agua', 'cerveza', 'vino'}
bebidas2.add('anis')  # añade un nuevo elemento 
print(bebidas2.issuperset(bebidas)) # True, bebidas es subconjunto
bebidas.remove('agua')  # borra elemento
print(bebidas & bebidas2)  # imprime elementos comunes
tapas = ['croquetas', 'solomillo', 'croquetas']  # define lista
conjunto = set(tapas)  # crea conjunto (sólo una de croquetas)
if 'croquetas' in conjunto:  # evalúa si croquetas está
conjunto1 = set('Python')  # define conjunto: P,y,t,h,o,n 
conjunto2 = set('Pitonisa')  # define conjunto: P,i,t,o,n,s,a
print(conjunto2 - conjunto1)  # aplica diferencia: s, i, a
print(conjunto1 | conjunto2)  # aplica unión: P,y,t,h,o,n,i,s,a 
print(conjunto1 & conjunto2)  # intersección: P,t,o,n
print(conjunto1 ^ conjunto2)  # diferencia simétrica: y,h,i,s,a