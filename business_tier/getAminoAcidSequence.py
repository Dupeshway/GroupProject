#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getAminoAcidSequence(input_type, input_value):
     amino_acid_sequence = db_query(dbArg5, input_type, input_value)
     
     return amino_acid_sequence
