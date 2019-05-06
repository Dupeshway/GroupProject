#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Obtain Amino Acid Sequence
File:getAminoAcidSequence.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to get Amino Acid Sequence from the database
--------------------------------------------------------------------------
Import libraries: import getDataFromDB
"""
import getDataFromDB

def getAminoAcidSequence(input_type, input_value):
      """Getting Amino Acid Sequence Function
     Input: input type and vaule in cofig 
     Output:Amino Acid Sequence
     """
     amino_acid_sequence = getDataFromDB(dbArg5, input_type, input_value)
     return amino_acid_sequence
