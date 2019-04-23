#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Import query from the database layer
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

def doEntrySummary(input_type, input_value):
     """ Input values and type if in infoList return listed in database 
               input_type= 
               input_value= """
     if input_type in infoList:
          return db_query('(*)', input_type, input_value)
     else:
          continue
