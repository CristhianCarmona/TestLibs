#!/usr/bin/python
# coding=utf-8

from Messages import *
from selenium.common.exceptions import *


__author__ = 'cristhian'


class Common(object):
    idiomas = ['EN', 'FR', 'BR', 'DE', 'IT']
    driver = None

    def set_driver_in_common(self, driver):
        """
        Set del driver en común
        """
        self.driver = driver

    def abrir_url(self, url=None, idioma=None):
        url = "http://{0}".format(str(url))
        self.driver.get(url)

    def seleccionar_plataforma(self, plataforma):
        lista_plataformas = ['Windows', 'Android', 'iPhone', 'Mac']
        assert plataforma in lista_plataformas, 'Plataforma no existe, debe ser %s' % str(','.join(lista_plataformas))
        plataforma_boton = self.driver.find_element_by_xpath("//div[contains(@class, 'selectDown sdbus')]")
        plataforma_boton.click()
        self.driver.get_screenshot_as_file("./capturaClick.png")

    def bucar_programa(self, programa):
        """
        Buscamos un programa en la barra principal de búsquedas
        :param programa: Nombre del programa o aplicación a buscar
        """
        text_form = self.driver.find_element_by_xpath("//input[@id='busqueda']")

