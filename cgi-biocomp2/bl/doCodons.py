#!/usr/bin/env python3
"""
Program:Condon
File:doCodons.py
Version:1.0
Date:May-7-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process DNA sequence 
--------------------------------------------------------------------------
from SQL_python_functions import *
import re
import doCodonDictionary
from configFile import *
"""
from SQL_python_functions import *
import re
import doCodonDictionary
from config import config as cg
import sys

sys.path.insert(0, '../')
sys.path.insert(0, '../db/')

""" Process codon of DNA Sequence""" 
def doCodons(dna_sequence):
     """ Functions to process DNA sequence codon
     input: dna sequence
     output: Codon for DNA seq"""
     p = re.compile(r'[ATCG]{3}')
     dna_sequence = db_query(cg.dbArg7, input_type, input_value)

     for i in range(0, len(dna_sequence), cg.codon_length):
          codon = dna_sequence[i:(i+cg.codon_length)]
          if p.match(codon):

               return codon
