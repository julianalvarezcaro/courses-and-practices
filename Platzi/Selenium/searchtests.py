"""Más ejemplos de búsquedas
"""

import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver =  webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
    
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)