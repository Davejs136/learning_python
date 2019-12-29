# !/usr/bin/python3
# -*- encoding: utf-8 -*-

class Volumen:
    """ Clase para controlar el volumen de un reproductor multimedia """
    def __init__(self):
        self.nivel = 3
        print('nivel', self.__class__.__name__, self.nivel)

    def subir(self):
        self.nivel += 1
        if self.nivel > 10:
            self.nivel = 10
        
        print('nivel', self.__class__.__name__, self.nivel)

    def bajar(self):
        self.nivel -= 1
        if self.nivel < 0:
            self.nivel = 0

        print('nivel', self.__class__.__name__, self.nivel)

    def silenciar(self):
        self.nivel = 0
        print('nivel', self.__class__.__name__, self.nivel)

class Graves(Volumen):
    pass