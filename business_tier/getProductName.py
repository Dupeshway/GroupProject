#!/usr/bin/env python3

"""
Program:Obtain Protein Product Name
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

""" Obtaining product Name"""

def getProductName(input_type, input_value):
     """ Function to obtain protein product name from the database
     input: database query type and value from the config file
     output:protein product name from database """
     
     product_name = db_query(dbArg4, input_type, input_value)
     return product_name

     if product_name == '':
          return 'Product Name Missing'
