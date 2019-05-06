#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain chromosomal location Name
File:getProductName.py
Version:1.0
Date:May-4-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to get chromosomal location name from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""
import getDataFromDB

def getChrLocation(input_type, input_value):
     """Getting chromosomal location Name Function
     Input: input type and vaule in cofig 
     Output:Protein Product Name
     """
     chromosomal_location = getDataFromDB(dbArg2, input_type, input_value)
     return chromosomal_location
