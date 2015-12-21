#!/usr/bin/python
# coding=utf-8

from selenium.common.exceptions import *
from Messages import *
from robot.api import logger


__author__ = 'cristhian'


class TextInput(object):
    """ leemos los diversos etiquetas de texto que nos devuelve el sistema|plataforma|aplicacion """

    def __init__(self):
        self.driver = None

    def set_driver_in_textinput(self, driver):
        """
        Set del driver en común
        """
        self.driver = driver

    def relleno_el_campo_con_etiqueta_con_texto(self, etiqueta_campo, texto):
        pass

    def relleno_campo_busqueda_con_el_texto(self, texto):
        try:
            form = self.driver.find_element_by_xpath('//form')
            campo_busqueda = form.find_element_by_xpath("//input[@id='busqueda']")
            campo_busqueda.send_keys(str(texto))
            logger.console(texto)
            logger.console(texto)
        except TimeoutException as e:
            print FIELD_NOT_FOUND.format(str('Busqueda'))
