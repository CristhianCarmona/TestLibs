#!/usr/bin/python
# coding=utf-8

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

__author__ = 'cristhian'


class ClassExample:
    """ imported class from Robot Framework IDE """

    def pasar_texto(self, texto):
        salida = 'Este texto(%s) es recibido desde el RIDE' % (str(texto))
        return salida

    def abrir_navegador(self, driver, url):
        #driver = webdriver.Firefox()

        #driver.set_window_size(1366, 768)  # (1920, 1080)
        #driver.maximize_window()
        driver.get(url)

        #assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium webdriver")
        elem.send_keys(Keys.RETURN)
        #driver.get_screenshot_as_file("./capturadesdeClassExample.png")
        #assert "No results found." not in driver.page_source
        driver.close()

