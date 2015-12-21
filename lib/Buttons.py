#!/usr/bin/python
# coding=utf-8

__author__ = 'cristhian'


class Buttons(object):
    """ En esta clase se colocan todas las interacciones sobre un botón o elementos similares a éstos """

    def __init__(self):
        self.driver = None

    def set_driver_in_buttons(self, driver):
        """
        Set del driver en común
        """
        self.driver = driver

    def clico_boton_con_nombre(self, nombre_boton):
        print nombre_boton

    def clico_boton_iniciar_sesion(self):
        pass

    def puntuo_cantidad_estrellas(self, numero_estrellas):
        print numero_estrellas

    def puntuo_cantidad_estrellas_la_pregunta_con_texto(self, pregunta, numero_estrellas):
        print pregunta + numero_estrellas