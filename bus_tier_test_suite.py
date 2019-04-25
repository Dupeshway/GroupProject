#!/usr/bin/env python3
import configFile

def doCodingRegionsAndDNA(input_type, input_value):
    """ Function for CodingRegionsAndDNA"""
     if input_type in infoList:
          sequenceDNA = db_query(dbArg1, input_type, input_value)
return db_query(output_type, input_type, input_value)

if __name__ == "__main__":
   import doctest
   doctest.testmod()

def doEntrySummary(input_type, input_value):
    """Entry Summary"""
    if input_type in infoList:
          return db_query('(*)', input_type, input_value)
    else:
          continue
if __name__ == "__main__":
   import doctest
   doctest.testmod()
   
def doFullSummary():
     """"Full summary of Database   """
     full_summary= db_summary()

if __name__ == "__main__":
   import doctest
   doctest.testmod()
