#!/usr/bin/python
# coding=utf-8

from Messages import *

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
        assert idioma.upper() in self.idiomas, LANGUAGE_NOT_FOUND.format(idioma.upper(), self.idiomas)
        if idioma == 'es':  # español por defecto
            url = 'http://{}'.format(url)
        else:
            url = 'http://{}/{}'.format(url, idioma)
        self.driver.get(url)

