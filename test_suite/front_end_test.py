"""
Program:Test Suite Front End
File:front_end_test.py
Version:1.0
Date:May-4-2019
Function: 
Author: Jeff Li
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: To test front end code
--------------------------------------------------------------------------
Usage: Check URL and search on the webpage
--------------------------------------------------------------------------
Import libraries: selenium
"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" Front End Test Suite"""
class FronTendSearch(unittest.TestCase):

Gene_id_code = ""
Products_protein = ""
Accession_number = ""
Seq_Locaton = ""

    def setUp(self):
        """ Open web page in firefox."""
        self.driver = webdriver.Firefox()
    def test_front_end(self):
        """Website Testing.
            Input: Url for fornt end
            Ouput Search pass or not"""
        driver = self.driver
        driver.get(" Need URL from front end ")
        self.assertIn("Gene_Header ", driver.title)
        elem = driver.find_element_by_id("Gene_id")
        elem.send_keys(Gene_id_code)
        elem = driver.find_element_by_id("Products")
        elem.send_keys(Products_protein)
        elem = driver.find_element_by_id("Accession")
        elem.send_keys(Accession_number)
        elem = driver.find_element_by_id("Seq_Locaton")
        elem.send_keys(Seq_Locaton)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

def tearDown(self):
    """Closing browser Window"""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
