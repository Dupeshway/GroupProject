#!/usr/bin/env python3
"""
Program:Obtain Chromosome Location
File:getChrLocation.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function for getting Chromosome Location from the database 
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

#""" Getting Chomosome Locaiton"""
def getChrLocation(input_type, input_value):
     """ Function to obtain Chromosome Location from the database
     input: database query Arg2, type, and value from the config file
     output:Chromosome Location from database"""
     chr_location = db_query(cg.dbArg2, input_type, input_value)
     if chr_location == '':
          return 'Chromosomal Location Missing'
     else:
          return chr_location
