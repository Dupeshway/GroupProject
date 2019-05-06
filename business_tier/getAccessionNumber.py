#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain Accession Number
File:getAccessionNumber.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to get Accession Number from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""
import getDataFromDB

def getAccessionNumber(input_type, input_value):
     """Getting Accession Number Function from the database
     Input: input type and vaule in cofig 
     Output:Amino Acid Sequence
     """
     accession_number = getDataFromDB(dbArg1, input_type, input_value)
     return accession_number
