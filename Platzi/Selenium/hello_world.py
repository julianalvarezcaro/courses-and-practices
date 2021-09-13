"""Estructura más básica de una implementación de Selenium.
Sólo abrimos una página y al cerramos.
"""

import unittest
from unittest.main import main
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    # Se encarga de preparar el entorno para el momento de la prueba
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    # Nuestro caso de prueba. Aquí definiremos pasos a probar
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    # Otro test :v
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    # Acciones al finalizar. Por lo general es cerrar el navegador después de la prueba-
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))