#!/usr/bin/python
# coding=utf-8

from Messages import *
from robot.api import logger
from selenium.common.exceptions import *


__author__ = 'cristhian'


class Common(object):
    idiomas = ['EN', 'FR', 'BR', 'DE', 'IT']
    driver = None

    def set_driver_in_common(self, driver):
        """ Set del driver en común """
        self.driver = driver

    def abrir_url(self, url, idioma=None):
        logger.info("Abrir url: " + url)
        self.driver.get(url)

    def buscar_programa(self, programa):
        """ Buscamos un programa en la barra principal de búsquedas """
        text_form = self.driver.find_element_by_xpath("//input[@id='busqueda']")

    def compruebo_que_aparece_mensaje_despues_de_busqueda(self, mensaje):
        """ Localiza mensaje que aparece justo después de la barra de búsqueda sea igual al que buscamos """
        try:
            cabecera = self.driver.find_element_by_xpath("//div[contains(@class, 'grid_12 tituloSEO inner mini vertical')]")
            mensaje_completo = cabecera.find_element_by_xpath("./*[contains(@class, 'bloqueEnLinea')]")
            assert mensaje.lower() in mensaje_completo.text.lower(), ELEMENT_NOT_FOUND.format(mensaje)
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format(mensaje))
            raise Exception(e.msg)
