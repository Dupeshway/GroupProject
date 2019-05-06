#!/usr/bin/env python3
from SQL_python_functions import *
import re
import doCodonDictionary
from configFile import *

def doCodons(dna_sequence):
     p = re.compile(r'[ATCG]{3}')
     dna_sequence = db_query(dbArg7, input_type, input_value)

     for i in range(0, len(dna_sequence), codon_length):
          codon = dna_sequence[i:(i+codon_length)]
          if p.match(codon):

               return codon
