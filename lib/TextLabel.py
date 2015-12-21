#!/usr/bin/python
# coding=utf-8

from Common import Common as common

__author__ = 'cristhian'


class TextLabel(object):
    def __init__(self):
        self.driver = common.driver

    def set_driver_in_textlabel(self, driver):
        """
        Set del driver en común
        """
        self.driver = driver

    def aparece_mensaje_texto_que_dice(self, texto):
        """ Busca una coincidencia de la cadena de texto de entrada con una cadena del sistema """
        print texto

    def clico_sobre_link_con_texto(self, nombre_link):
        """ Clica sobre el link con el texto que indica el usuario """
        print nombre_link

    def activo_el_check_con_texto(self, texto):
        """ Activa un check si no está activado. Si está activado lo deja así """
        print texto

    def clico_check_circular_con_texto(self, texto):
        """ Selecciono un check radio con nombre determinado """
        print texto

    def selecciono_dia_del_desplegable(self, dia_numero):
        print dia_numero

    def selecciono_mes_del_desplegable(self, mes_texto):
        print mes_texto

    def selecciono_anio_del_desplegable(self, anio_numero):
        print anio_numero