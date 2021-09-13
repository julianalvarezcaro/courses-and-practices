"""Manejo de navegación en el navegador (avanzar o retroceder en el historial)
"""

import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver =  webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(2)
        driver.forward()
        sleep(2)
        driver.refresh()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)