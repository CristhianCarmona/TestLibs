#!/usr/bin/python
# coding=utf-8

__author__ = 'cristhian'


class Setup(object):
    """
    Esta clase sirve para pasar un browser desde la libreria Selenium2Library a las nuestras
    permitiendonos compartir el mismo browser por parte de nuestras funciones personalizadas y las definidas.
    """
    message = "This is a message"

    def __init__(self):
        self._browser = None

    def set_browser(self, browser):
        self._browser = browser

    def get_browser(self):
        return self._browser

    def imp(self):
        return self.message

    def imp2(self):
        return self.message