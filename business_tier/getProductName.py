#!/usr/bin/env python3

"""
Program:Processing codon dicitonary
File:getProductName.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function for getting Protein Product Name from the database 
--------------------------------------------------------------------------
imported Libraries:
from SQL_python_functions import *
from configFile import *
"""
from SQL_python_functions import db_query
from configFile import *

""" Obtaingint product Name"""

def getProductName(input_type, input_value):
     """ Function to obtain protein product name from the database
     input: database query with Arg4, type and value from the config file
     output:protein product name from database """
     
     product_name = db_query(dbArg4, input_type, input_value)

     return product_name
