#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain DNA Sequence
File:getDNA.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function for getting DNA Sequence from the database
--------------------------------------------------------------------------
Import libraries: 
from SQL_python_functions import db_query
from configFile import *
"""
from SQL_python_functions import db_query
from configFile import *

def getDNA(input_type, input_value):
     """ Function to obtain protein GeneID  from the database
     input: database query type and value from the config file
     output:dna_sequence from database"""
     dna_sequence = db_query(dbArg7, input_type, input_value)
     
     return dna_sequence
