#!/usr/bin/env python3
from SQL_python_functions import *
import doCodons
import doCodonDictionary

def doLocalCodonUsage(input_type, input_value):
     d = doCodonDictionary
     dna_sequence = db_query(dbArg7, input_type, input_value)
     codon_count = 0
     codon = doCodons(dna_sequence)

     for key in d:
          if key == codon:
               d[key] += 1
               codon_count += 1

     for key in d:
          d[key] = round((d[key]/codon_count), 3)

     return d
