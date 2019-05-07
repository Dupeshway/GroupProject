#!/usr/bin/env python3

"""
Program:Local Codon Usage
File:doLocalCodonUsage.py
Version:1.0
Date:May-7-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process Local Codon usage
--------------------------------------------------------------------------
from SQL_python_functions import *
import doCodons
import doCodonDictionary
from config import config as cg
import sys
"""

from SQL_python_functions import *
import doCodons
import doCodonDictionary
from config import config as cg
import sys

sys.path.insert(0, '../db/')

def doLocalCodonUsage(input_type, input_value):
     """ Process Coordinate ends from the Local codon usage
     Input: input type and value in config file
     Output: count for codons"""
     d = doCodonDictionary
     dna_sequence = db_query(cg.dbArg7, input_type, input_value)
     codon_count = 0
     codon = doCodons(dna_sequence)

     for key in d:
          if key == codon:
               d[key] += 1
               codon_count += 1

     for key in d:
          d[key] = round((d[key]/codon_count), 3)

     return d
