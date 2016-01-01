#!/usr/bin/python
# coding=utf-8

from robot.api import logger

__author__ = 'cristhian'


class Setup(object):
    """ Esta clase sirve para pasar un browser desde la libreria Selenium2Library a las nuestras
    permitiendonos compartir el mismo browser por parte de nuestras funciones personalizadas y las definidas. """
    message = "This is a message"

    def __init__(self, *args):
        """ Acepta arg desde RIDE """
        logger.console("*** Numero de argumentos %s ***" % str(len(args)))
        logger.console("*** Argumentos leidos desde RIDE ***")
        for arg in args:
            logger.console("***  %s ***" % arg)

        self.browser = args[0]

    def set_browser(self, browser):
        self.browser = browser

    def get_browser(self):
        return self.browser
