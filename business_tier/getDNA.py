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
Description: Funciton for getting DNA Sequence from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""
import getDataFromDB

def getDNA(input_type, input_value):
     """Getting DNA Sequence Name Function
     Input: input type and vaule in cofig 
     Output: DNA Sequence
     """
     dna_sequence = getDataFromDB(dbArg7, input_type, input_value)
     return dna_sequence
