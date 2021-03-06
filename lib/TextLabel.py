#!/usr/bin/python
# coding=utf-8

from Common import Common as common
from selenium.common.exceptions import *
from robot.api import logger
from Messages import *
from random import randint

__author__ = 'cristhian'


class TextLabel(object):
    def __init__(self):
        self.driver = common.driver

    def set_driver_in_textlabel(self, driver):
        """ Set del driver en común """
        self.driver = driver

    def aparece_mensaje_texto_que_dice(self, texto):
        """ Busca una coincidencia con el mensaje que aparece justo después de la cabecera """
        try:
            mensaje = self.driver.find_element_by_xpath("//h1")
            assert texto in mensaje.text, "'%s' no coincide con el texto encontrado '%s'" %(texto, mensaje)
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Texto: ' + texto))
            raise Exception(e.msg)

    def aparece_mensaje_error_mail(self, texto_error):
        """ Localiza el mensaje de error que devuelve el campo del email"""
        try:
            label_error = self.driver.find_element_by_xpath("//p[@class='colorRojo']")
            assert texto_error in label_error.text, "Textos no coinciden %s != %s" % (texto_error, label_error.text)
        except (TimeoutException, NoSuchElementException) as e:
            fichero = 'email_incorrecto' + str(randint(0, 9999)) + '.png'
            self.driver.get_screenshot_as_file(fichero)
            # si hay algún error cerramos sesión del usuario logueado para que no afecte al resto de pruebas
            self.driver.get('http://www.portalprogramas.com/comunidad/cerrarSesion')
            logger.error(ELEMENT_NOT_FOUND.format('class: colorRojo'))
            raise Exception('Compruebe captura pantalla con el error: ' + fichero)

    def clico_sobre_link_con_texto(self, nombre_link):
        """ Clica sobre el link con el texto que indica el usuario """
        try:
            enlace = self.driver.find_element_by_link_text(nombre_link)
            enlace.click()
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Link: ' + nombre_link))
            raise Exception(e.msg)

    def activo_el_check_con_nombre(self, nombre):
        """ Activa un check dado su nombre """
        try:
            checkbox = self.driver.find_element_by_name(nombre)
            checkbox.click()
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Name: ' + nombre))
            raise Exception(e.msg)

    def clico_en_salir(self):
	""" Cierra sesión de usuario mediante URL """
        try:
            url = 'http://www.portalprogramas.com/comunidad/cerrarSesion'
            self.driver.get(url)
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format(url))
            raise Exception(e.msg)

    def clico_check_circular_con_texto(self, texto):
	logger.info('#TODO')

    def selecciono_dia_del_desplegable(self, dia_numero):
        logger.info('#TODO')

    def selecciono_mes_del_desplegable(self, mes_texto):
        logger.info('#TODO')

    def selecciono_anio_del_desplegable(self, anio_numero):
        logger.info('#TODO')
