#!/usr/bin/env python3
#from database_layer import db_query
import configFile

def getDataFromDB(var1, var2, var3):
     data = ''
     for x in db_query(var1, var2, var3):
          data += x
     return data
