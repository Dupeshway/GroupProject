#!/usr/bin/env python3
"""
Program:Test Suite Front End
File:front_end_test.py
Version:1.0
Date:May-4-2019
Function: 
Author: Jeff Li
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description:selenium To test front end code
--------------------------------------------------------------------------
Usage: Used selenium to check URL and search on the webpage
--------------------------------------------------------------------------
Import libraries: selenium
"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" Front End Test Suite"""
class FronTendSearch(unittest.TestCase):

Gene_id = ""
Protein_product_names = ""
Accession_number = ""
Chromosomal location = ""

    def setUp(self):
        """ Open web page in firefox."""
        self.driver = webdriver.Firefox()
    def test_front_end(self):
        """ Web testing for fron end
            Input: Url for fornt end
            Ouput Search pass or not"""
        driver = self.driver
        driver.get(" http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/wc005/cgi_script.py")
        self.assertIn("Gene_Header ", driver.title)
        elem = driver.find_element_by_id("Gene")
        elem.send_keys(Gene_id_code)
        elem = driver.find_element_by_id("Protein")
        elem.send_keys(Protein product names)
        elem = driver.find_element_by_id("Accession")
        elem.send_keys(Accession_number)
        elem = driver.find_element_by_id("Chromosomal")
        elem.send_keys(Chromosomal location )
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

def tearDown(self):
    """Closing browser Window"""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
