#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain CDS Location
File:getLocationCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to get data from the database
--------------------------------------------------------------------------
Import libraries: import configFile
"""
import configFile

def getDataFromDB(var1, var2, var3):
     """Getting Raw Data from database layer
     Input: var1, var2, and var3
     Output:Data from the data base
     """
     data = ''
     for x in db_query(var1, var2, var3):
          data += x
     return data
