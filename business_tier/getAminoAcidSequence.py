#!/usr/bin/env python3
#from database_layer import db_query
import getDataFromDB

def getAminoAcidSequence(input_type, input_value):
     amino_acid_sequence = getDataFromDB(dbArg5, input_type, input_value)
     return amino_acid_sequence
