#!/usr/bin/python
# coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from robot.api import logger
from Messages import *
import inspect
import time

__author__ = 'cristhian'


class Buttons(object):
    """ En esta clase se colocan todas las interacciones sobre un botón o elementos similares a éstos """

    def __init__(self):
        self.driver = None

    def set_driver_in_buttons(self, driver):
        """ Set del driver en común """
        self.driver = driver

    def clico_sobre_icono_lupa(self):
        try:
            form = self.driver.find_element_by_xpath('//form')
            barra_busqueda = form.find_element_by_xpath("//input[@class='botonBuscar busb']")
            barra_busqueda.click()
            # FUNCIONA
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Lupa/Buscar'))
            raise Exception(e.msg)

    def clico_sobre_boton_descargar(self):
        try:
            area_detalle = self.driver.find_element_by_xpath("//div[@class='listadoElementos programas grande']")
            area_detalle.click()
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Descargar'))
            raise Exception(e.msg)

    def clico_boton_iniciar_sesion(self):
        """ Hace click sobre el botón 'Iniciar Sesion' ubicado en la cabecera de la página principal """
        try:
            boton_sesion = self.driver.find_element_by_xpath("//span[@class='icono iniciarSesion']")
            boton_sesion.click()
            # FUNCIONA
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Icono iniciar sesion'))
            raise Exception(e.msg)

    def clico_boton_con_nombre(self, nombre_boton):
        """ Dado el nombre de un botón lo localiza y hace click sobre él """
        try:
            boton = self.driver.find_element_by_xpath("//input[@value='" + nombre_boton + "']")
            boton.submit()
            time.sleep(1)
            # self.driver.get_screenshot_as_file("validacionmailerror.png")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(ELEMENT_NOT_FOUND.format('Boton: ' + nombre_boton))
            raise Exception(e.msg)

    def puntuo_cantidad_estrellas(self, numero_estrellas):
        logger.info('#TODO')

    def puntuo_cantidad_estrellas_la_pregunta_con_texto(self, pregunta, numero_estrellas):
        logger.info('#TODO')