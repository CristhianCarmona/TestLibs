#!/usr/bin/python
# coding=utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from robot.api import logger
from Messages import *

__author__ = 'cristhian'


class TextMenu(object):
    def __init__(self):
        self.driver = None

    def set_driver_in_textmenu(self, driver):
        """ Set del driver en común """
        self.driver = driver

    def me_situo_sobre_opcion_menu_principal(self, opcion):
        logger.info('#TODO')

    def clico_subopcion_con_nombre(self, subopcion):
        logger.info('#TODO')

    def hago_click_sobre_icono_seleccionar_plataforma(self):
	""" Hace click directamente sobre el icono de los sistemas operativos de la barra de búsqueda"""
        try:
            form = self.driver.find_element_by_xpath('//form')
            barra_busqueda = form.find_element_by_xpath(".//input[@id='opcionMenuSelected_mac'] and //span[@class='icono verMas']")
            barra_busqueda.click()
        except TimeoutException as e:
            logger.error(PLATFORM_NOT_FOUND.format(str('Busqueda')))
            raise Exception(e.msg)

    def selecciono_plataforma_con_nombre(self, plataforma):
        """ Clica sobre el desplegable y elege una plataforma disponible """
        try:
            lista_plataformas = ['Windows', 'Android', 'iPhone', 'Mac']
            assert plataforma in lista_plataformas, PLATFORM_NOT_FOUND.format(plataforma,
                                                                              str(','.join(lista_plataformas)))

            form = self.driver.find_element_by_xpath('//form')
            barra_busqueda = form.find_element_by_xpath(".//span[contains(@class, 'iconoMenu verMas')]")

            # establecemos una espera explícita
            plataforma_boton = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'selectDown sdbus')]"))
            )
            plataforma_boton.click()
            elegir_plataforma = self.driver.find_element_by_xpath("//span[contains(@class, 'txt') and "
                                                                  "normalize-space(text())='" + plataforma + "']")
            elegir_plataforma.click()
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(PLATFORM_NOT_FOUND.format(plataforma, lista_plataformas))
            raise Exception(e.msg)
