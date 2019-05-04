#!/usr/bin/env python3
#from database_layer import db_query
import configFile
import re

def doSelectCDS(input_type, input_value):
     
     dna_sequence = db_query(dbArg7, input_type, input_value)
     chr_location = db_query(dbArg2, input_type, input_value)
     
     coordinate_start = re.findall(r'(\d+)\-', chr_location)
     coordinate_end = re.findall(r'\-(\d+)', chr_location)

     dna_selected_cds = ''

     count_start = -1
     for x in coordinate_start:
          dna_selected_cds = dna_sequence[:int(x)+count_start] \
                             + char_start + dna_sequence[int(x)+count_start:]
          count_start += 1

     count_end = 1
     for x in coordinate_end:
          dna_selected_cds = dna_selected_cds[:int(x)+count_end] \
                             + char_end + dna_selected_cds[int(x)+count_end:]
          count_end += 2
     
     return dna_selected_cds
