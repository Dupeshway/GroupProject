#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain Chromosome Location
File:getLocationCDS.py
Version:1.0
Date:May-4-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to getting Chromosome Location from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""

import getDataFromDB

def getGeneID(input_type, input_value):
      """Getting Gene ID Function from Database
     Input: input type and vaule in cofig 
     Output:Gene ID
     """
     gene_id = getDataFromDB(dbArg3, input_type, input_value)
     return gene_id
