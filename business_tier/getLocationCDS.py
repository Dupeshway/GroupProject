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
from configFile import *
"""
from SQL_python_functions import db_query
from configFile import *

def getLocationCDS(input_type, input_value):
     cds_location = db_query(dbArg6, input_value, output_value)
     
     return cds_location

