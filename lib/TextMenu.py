#!/usr/bin/python
# coding=utf-8


__author__ = 'cristhian'


class TextMenu(object):

    def __init__(self):
        self.driver = None

    def set_driver_in_textmenu(self, driver):
        """
        Set del driver en común
        """
        self.driver = driver

    def me_situo_sobre_opcion_menu_principal(self, opcion):
        pass

    def clico_subopcion_con_nombre(self, subopcion):
        pass

