#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Import query from the database layer
File:doEntrySummary.py
Version:
Date:
Author: Margherita Martorana, Documentation(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------
Usage: Import from the database layer
--------------------------------------------------------------------------
Import libraries: configFile
import configFile
"""

import configFile

""" Entry Summary Function """

def doEntrySummary(input_type, input_value):
          """  Pull from database layer for database query
               input_type= 
                    infoType1 = 'gene_id'
                    infoType2 = 'acc_number'
                    infoType3 = 'product_name'
                    infoType4 = 'chr_location'
               input_value= 
               in info list returns query"""
     if input_type in infoList:
          return db_query('(*)', input_type, input_value)
     else:
          continue