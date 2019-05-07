#!/usr/bin/env python3
"""
Program:Accession Number
File:getAccessionNumber.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function for getting Accession Number from the database 
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

#""" Getting Accession Number"""
def getAccessionNumber(input_type, input_value):
     """ Function to obtain accession number from the database
     input: database query with Arg4, type and value from the config file
     output: accession numberfrom database """
     accession_number = db_query(cg.dbArg1, input_type, input_value)

     return accession_number
