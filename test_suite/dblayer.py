#!/usr/bin/env python3

"""
Program:Test Suite Database layer
File:dblayer.py
Version:1.0
Date:May-4-2019
Function: 
Author: Jeff Li
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description:selenium To test for database layer
--------------------------------------------------------------------------
Usage: Testing for database layer 
--------------------------------------------------------------------------
import unittest
import re
from config import config as cg
from file_management import file_management as fm
from cleaning_data import clean_data as cl
"""

import unittest
import re
from config import config as cg
from file_management import file_management as fm
from cleaning_data import clean_data as cl


class test_parse_data(unittest.TestCase):

    """
    testing parse data
    """
    global dna
    dna = "GCG"
    global protein_sequence
    protein_sequence = "LEU"
    global ac_number
    ac_number = "12324.3"
    
    def test_parse_prot_trans(self,dna):
        pass
        #camptures the full dna sequence
    def test_parse_product_name(self, protein_sequence):
        pass
        # Captures the protein product name
    def test_simpleparse_acc_no(self, info):
        pass
        # capture lines that begin with the string: Accession

    def test_parse_acc_no(self, ac_number):
        pass
        #capture lines that begin with the string: Accession
    
    def test_parse_dna_seq(self, dna):
        pass
        #captures the full dna sequence

if __name__ == '__main__':
    unittest.main()

import pymysql.cursors

class test_sql_query(unittest.TestCase):
        """
        testing sql query
        """
    
    def test_db_query(self):
        pass
        #Retreive search query 
    def test_db_summary(self):
        pass 
        #Returning entire record assoiciated with Accession no.
if __name__ == '__main__':
    unittest.main()
