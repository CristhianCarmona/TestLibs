#!/usr/bin/python
# coding=utf-8

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from robot.api import logger

__author__ = 'cristhian'


class SettingsBrowser(object):
    """ Gestionamos las configuraciones de los navegadores más usados: firefox, chrome y phantomjs"""

    def __init__(self):
        self._capabilites = None
        self.driver = None
        self.driver_p = None

    def set_configuraciones_navegador(self, tipo_nav):
        if tipo_nav.upper() == 'FIREFOX':
            # Copiamos la configuracion por defecto del navegador
            self._capabilites = DesiredCapabilities.FIREFOX.copy()

            # Sistema operativo
            self._capabilites['platform'] = 'ANY'

            # Nombre del navegador
            self._capabilites['browsername'] = 'firefox'

            # Version del navegador
            self._capabilites['version'] = '41.0.2'

            # JavaScript activado o no
            self._capabilites['javascriptEnabled'] = True

            # Navegador marionette activado o no
            self._capabilites['marionette'] = False

        elif tipo_nav.upper() == 'CHROME':
            logger.console('#TODO Using broowser Chrome')

        elif tipo_nav.upper() == 'PHANTOMJS':
            logger.console('#TODO Using browser Phantomjs')

        return self._capabilites

    def get_browser_phantomjs(self):
        """ Retornamos el navegador que se crea con las librerias de Selenium2Library para PhantomJS"""
        return self.driver_p

    def get_browser_firefox(self):
        """ Retornamos el navegador que se crea con las librerias de Selenium2Library para firefox"""
        return self.driver

    def set_custom_browser_firefox_in_settingsbrowser(self, browser):
        """ Establecemos el navegador que se crea con las librerias de Selenium2Library para Firefox"""
        self.driver = browser

    def set_custom_browser_phantomjs(self, browser):
        """ Establecemos el navegador que se crea con las librerias de Selenium2Library para PhantomJS"""
        self.driver = browser

    def close_browser_firefox(self):
        self.driver.close()

