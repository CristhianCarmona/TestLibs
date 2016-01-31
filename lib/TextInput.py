#!/usr/bin/python
# coding=utf-8

from selenium.common.exceptions import *
from Messages import *
from robot.api import logger


__author__ = 'cristhian'


class TextInput(object):
    """ Leemos los diversos etiquetas de texto que nos devuelve el sistema|plataforma|aplicacion """

    def __init__(self):
        self.driver = None

    def set_driver_in_textinput(self, driver):
        """ Set del driver en común """
        self.driver = driver

    def relleno_el_campo_de_nombre_interno_con_texto(self, nombre_campo_interno, texto):
        """ Rellena con datos el campo de texto buscandolo por el placeholder(texto interno del campo) """
	logger.info('#TODO')	
	
    def relleno_campo_busqueda_con_el_texto(self, texto):
        """ Rellena el campo de búsqueda con el texto dado """
        try:
            form = self.driver.find_element_by_xpath('//form')
            campo_busqueda = form.find_element_by_xpath("//input[@id='busqueda']")
            campo_busqueda.clear()
            campo_busqueda.send_keys(str(texto))
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(FIELD_NOT_FOUND.format('Busqueda'))
            raise Exception(e.msg)

    def relleno_campo_texto_con_etiqueta_con_texto(self, etiqueta, texto):
        """ Rellena un campo de texto buscando su etiqueta como nombre """
        try:
            # localizamos la etiqueta del text box que buscamos
            form = self.driver.find_element_by_xpath('//form')
            label = form.find_element_by_xpath('//*[contains(@class, "ocultarUsuarios")]'
                                               '//strong[normalize-space(text())="' + etiqueta + '"]')

            # después de localizar la etiqueta del text box buscamos su hermano más inmediato que es donde
            # se ubica el text box input
            textbox = label.find_element_by_xpath('./following::input')
            textbox.clear()
            textbox.send_keys(texto)
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(FIELD_NOT_FOUND.format(etiqueta))
            raise Exception(e.msg)
