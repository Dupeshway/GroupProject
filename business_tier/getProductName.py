#!/usr/bin/env python3
#from database_layer import db_query
import getDataFromDB

def getProductName(input_type, input_value):
     product_name = getDataFromDB(dbArg4, input_type, input_value)
     return product_name
