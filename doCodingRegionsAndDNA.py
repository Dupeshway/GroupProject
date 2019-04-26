#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Coding Regions And DNA
File:
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

def doCodingRegionsAndDNA(input_type, input_value):
     """ Function for DNA coding Resgion and DNA
          input_type=
               infoType1 = 'gene_id'
               infoType2 = 'acc_number'
               infoType3 = 'product_name'
               infoType4 = 'chr_location'
          input_value=
          returnsequenceDNA if in list
          
          """
     if input_type in infoList:
          sequenceDNA = db_query(dbArg1, input_type, input_value)


          return db_query(output_type, input_type, input_value)
