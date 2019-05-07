#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:End CDS
File:doEndCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to Process Coordine ends from the CDS location
--------------------------------------------------------------------------
Import libraries:
import re
import getLocationCDS
"""
import re
import getLocationCDS
""" End of CDS""" 
def getEndCDS(input_value, input_value):
     """ Process Coordine ends from the CDS location 
     Input: input type and vaule in cofig file
     Output:codinate end of CDS location """
     x = getLocationCDS(input_value, input_value)
     coordinate_end = re.findall(r'\-(\d+)', x)

     return coordinate_end
