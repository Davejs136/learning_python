# !/usr/bin/python3
# -*- encoding: utf-8 -*-

class Factura():
    __tasa = 19 # Ocultar attr "__nombreVariable"

    def __init__(self, unidad, precio):
        self.unidad = unidad
        self.precio = precio

    def a_pagar(self):
        total = self.unidad * self.precio
        impuesto = total * self.__tasa / 100
        return (total + impuesto)

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def getnombre(self):
        return self.__nombre

    def getsalario(self):
        return self.__salario

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setsalario(self, salario):
        self.__salario = salario

    def delnombre(self):
        del self.__nombre

    def delsalario(self):
        del self.__salario

empleado1 = Empleado('Daniel', 1200000)
print(empleado1.getnombre())