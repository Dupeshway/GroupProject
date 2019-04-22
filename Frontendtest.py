#!/usr/bin/env python3

"""
Program:Test SuiteFront End
File:
Version:
Date:
Function: 
Author: Jeff Li
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: To test front end code
--------------------------------------------------------------------------
Usage:
--------------------------------------------------------------------------
Import libraries: selenium
"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FronTendSearch(unittest.TestCase):

    def setUp(self):
        """ open web page in firefox"""
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        """ open URL and search for  (tb filled in once front end is ready)"""
        driver = self.driver
        driver.get("  front end URL")
        self.assertIn("Chromosome 8", driver.title)
        elem = driver.find_element_by_name("accesion")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
