#!/usr/bin/env python3
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
from SQL_python_functions import db_query
from config import config as cg
import sys
"""

from SQL_python_functions import db_query
from config import config as cg
import sys

sys.path.insert(0, '../db/')
sys.path.insert(0, '../')

#""" Getting Gene ID"""
def getGeneID(input_type, input_value):
     """ Function to obtain protein GeneID  from the database
     input: database query Arg3, type, and value from the config file
     output:Gene ID from database"""
     gene_id = db_query(cg.dbArg3, input_type, input_value)
     if gene_id == '':
          return 'Gene ID missing'
     else:
          return gene_id

