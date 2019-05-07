#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

"""
Program:Obtain GeneID
File:getGeneID.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function for getting GeneID from the database 
--------------------------------------------------------------------------
imported Libraries:
from SQL_python_functions import *
from configFile import *
"""

""" Getting Gene ID"""
def getGeneID(input_type, input_value):
     """ Function to obtain protein GeneID  from the database
     input: database query Arg3, type, and value from the config file
     output:Gene ID from database"""
     gene_id = db_query(dbArg3, input_type, input_value)
     if gene_id == '':
          return 'Gene ID missing'
     else:
          return gene_id

