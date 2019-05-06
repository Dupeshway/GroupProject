#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain chromosomal location Name
File:getChrLocation.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to get chromosomal location name from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""
import getDataFromDB

def getChrLocation(input_type, input_value):
     """Getting chromosomal location Function
     Input: input type and vaule in cofig 
     Output:chromosomal location
     """
     chromosomal_location = getDataFromDB(dbArg2, input_type, input_value)
     return chromosomal_location
