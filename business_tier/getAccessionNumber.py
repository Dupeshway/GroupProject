#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getAccessionNumber(input_type, input_value):
     accession_number = db_query(dbArg1, input_type, input_value)

     return accession_number
