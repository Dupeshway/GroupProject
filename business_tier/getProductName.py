#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain Protein Product Name
File:getProductName.py
Version:1.0
Date:May-4-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to get Protein Product name from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""

import getDataFromDB
def getProductName(input_type, input_value):
     """Getting Protein Product Name Function
     Input: input type and vaule in cofig 
     Output:Protein Product Name
     """
     product_name = getDataFromDB(dbArg4, input_type, input_value)
     return product_name
