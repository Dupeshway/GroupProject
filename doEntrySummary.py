#!/usr/bin/env python3
#from database_layer import db_query
import configFile

def doEntrySummary(input_type, input_value):
     if input_type in infoList:
          return db_query('(*)', input_type, input_value)
     else:
          continue
