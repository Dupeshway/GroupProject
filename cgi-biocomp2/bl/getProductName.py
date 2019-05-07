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
from SQL_python_functions import db_query
from config import config as cg
import sys
"""
from SQL_python_functions import db_query
from config import config as cg
import sys

sys.path.insert(0, '../db/')
sys.path.insert(0, '../')

""" Obtaining product Name"""

def getProductName(input_type, input_value):
     """ Function to obtain protein product name from the database
     input: database query type and value from the config file
     output:protein product name from database """
     
     product_name = db_query(cg.dbArg4, input_type, input_value)
     if product_name == '':
          return 'Product Name Missing'
     else:
          return product_name
