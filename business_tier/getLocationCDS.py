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
Description: Funciton to getting Chromosome Location from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""
import getDataFromDB

def getLocationCDS(input_value, input_value):
          """Getting CDS Location Function from database layer
     Input: input type and vaule in cofig 
     Output:CDS Location
     from Database
     """
     cds_location = getDataFromDB(dbArg6, input_value, output_value)
     return cds_location

