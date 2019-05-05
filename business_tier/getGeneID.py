#!/usr/bin/env python3
#from database_layer import db_query
import getDataFromDB

def getGeneID(input_type, input_value):
     gene_id = getDataFromDB(dbArg3, input_type, input_value)
     return gene_id
