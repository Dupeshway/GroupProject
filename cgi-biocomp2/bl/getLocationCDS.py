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
Description: Function to getting Chromosome Location from the database
--------------------------------------------------------------------------
Import libraries: 
from SQL_python_functions import db_query
from config import config as cg
import sys
"""
from SQL_python_functions import db_query
from config import config as cg
import sys

sys.path.insert(0, '../db/')
sys.path.insert(0, '../')

#"""CDS location"""
def getLocationCDS(input_type, input_value):
    """ Function to obtain CDS Location from the database
    input: database query with Arg4, type and value from the config file
    output: CDS Location from database """
    cds_location = db_query(cg.dbArg6, input_value, output_value)
     
    return cds_location
