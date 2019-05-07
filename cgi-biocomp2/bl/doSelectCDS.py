#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Select CDS
File:doSelectCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process select CDS region
--------------------------------------------------------------------------
Import libraries:
from config import config as cg
import doStartCDS
import doEndCDS
import getDNA
import re
"""

from config import config as cg
import doStartCDS
import doEndCDS
import getDNA
import sys

sys.path.insert(0, '../')

#""" Select CDS"""
def doSelectCDS(input_type, input_value):
      """ Process select CDS from the getLocationCDS
      Input: input type and value in config 
      Output:selected DNA Coordinate """
      start_cds = doStartCDS(input_type, input_value)
      end_cds = doEndCDS(input_type, input_value)
      dna_sequence = getDNA(input_type, input_value)

      dna_selected_cds = ''

      count_start = -1
      for x in start_cds:      #adding start cds character
           dna_selected_cds = dna_sequence[:int(x)+count_start] \
                             + cg.cds_start_char + dna_sequence[int(x)+count_start:]
           count_start += 1

      count_end = 1
      for x in end_cds:        #adding end cds character
           dna_selected_cds = dna_selected_cds[:int(x)+count_end] \
                             + cg.cds_end_char + dna_selected_cds[int(x)+count_end:]
           count_end += 2
     
      return dna_selected_cds
