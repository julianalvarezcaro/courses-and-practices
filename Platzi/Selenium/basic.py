"""Este archivo es para, a partir de este, crear otrs archivos.
Su único propósito es pser copiado y pegado como base.
"""

import unittest
from selenium import webdriver

class Basic(unittest.TestCase):

    def setUp(self) -> None:
        self.driver =  webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)