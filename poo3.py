# !/usr/bin/python3
# -*- encoding: utf-8 -*-

""" Saber que metodos llama python primero """

class Clase_A():
  def metodo1(self):
    print("Clase_A.metodo1()")

  def metodo3(self):
    print("Clase_A.metodo3()")

  def metodo4(self):
    print("Clase_A.metodo4()")

class Clase_A1(Clase_A):
  def metodo1(self):
    print("Clase_A1.metodo1()")

  def metodo2(self):
    print("Clase_A1.metodo2()")

class Clase_A2(Clase_A):
  def metodo1(self):
    print("Clase_A2.metodo1()")

  def metodo3(self):
    print("Clase_A2.metodo3()")

class Clase_X(Clase_A1, Clase_A2):
  def metodo1(self):
    print("Clase_X.metodo1()")

obj1 = Clase_X() # creacion de una instancia
obj1.metodo1() # Clase_X.metodo1()
obj1.metodo2() # Clase_A1.metodo2()
obj1.metodo3() # Clase_A2.metodo3()
obj1.metodo4() # Clase_A.metodo4()

print("")
# __mro__ devuelve una tupla con las clases
# por su orden de resolucion de metodos
# de abajo a arriba
# de izq a derecha
print(Clase_X.__mro__)

class Clase_I(object):
    def __init__(self):
        self.var1 = 1
        print('Clase_I.__init__')
        
    def metodo1(self):
        self.var2 = 1
        print('Clase_I.metodo1()')

class Clase_II(object):
    def __init__(self):
        self.var1 = 2
        print('Clase_II.__init__')
        
    def metodo1(self):
        self.var2 = 2
        print('Clase_II.metodo1()')
        
class Clase_III(Clase_I, Clase_II):
    def __init__(self):
        self.var1 = 3
        print('Clase_III.__init__', end = ', ')
        super().__init__()
        
    def metodo1(self):
        print('Clase_III.metodo1()', end = ', ')
        super().metodo1()
        self.var2 = 3

class Clase_IV(Clase_II, Clase_I):
    def __init__(self):
        self.var1 = 4
        print('Clase_IV.__init__', end = ', ')
        super().__init__()
        
    def metodo1(self):
        print('Clase_IV.metodo1()', end = ', ')
        super().metodo1()
        self.var2 = 4

# Al crear objeto1 y objeto2 en el método __init__ se 
# invoca también el método __init__ de su clase superior

objeto1 = Clase_III()  # Clase_III.__init__, Clase_I.__init__
objeto2 = Clase_IV()  # Clase_IV.__init__, Clase_II.__init__

# El atributo especial __mro__ retorna una tupla
# con las clases ordenadas de izquierda a derecha
# que indican la prioridad en la herencia.
# Mientras en la Clase_III tiene mayor prioridad en 
# la herencia la Clase_I que la Clase_II; en la Clase_IV
# es al revés

print(Clase_III.__mro__)
# (class '__main__.Clase_III', class '__main__.Clase_I', 
#  class '__main__.Clase_II', class 'object')
 
print(Clase_IV.__mro__)  
# (class '__main__.Clase_IV', class '__main__.Clase_II', 
#  class '__main__.Clase_I', class 'object')

# Al llamar al metodo1 de objeto1 y objeto2 se invoca 
# también el equivalente de su clase superior

objeto1.metodo1()  # Clase_III.metodo1(), Clase_I.metodo1()
objeto2.metodo1()  # Clase_IV.metodo1(), Clase_II.metodo1()

# Al acceder a la variable var1 de objeto1 y objeto2
# se obtiene el valor que tiene en la clase superior
# porque en el método __init__ de su clase, DESPUÉS de
# la asignación, se invoca con la función super() al 
# método __init__ de la clase superior donde se realiza
# una asignación a la misma variable.

print(objeto1.var1)  # 1
print(objeto2.var1)  # 2

# Al acceder a la variable var2 de objeto1 y objeto2
# se obtiene el valor que tiene en su clase 
# porque aunque en el método metodo1() de su clase 
# se invoca con la función super() a su equivalente de
# la clase superior, la invocación se realiza ANTES
# de la asignación a dicha variable.

print(objeto1.var2) # 3
print(objeto2.var2) # 4