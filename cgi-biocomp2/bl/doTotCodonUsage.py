#!/usr/bin/env python3
"""
Program:Tot Condon Usage
File:doTotCodonUsage.py
Version:1.0
Date:May-7-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to calculate Total Codon Usage
--------------------------------------------------------------------------
from config import config as cg
from SQL_python_functions import *
import doCodonDictionary
import doCodons
import sys
"""

from config import config as cg
from SQL_python_functions import *
import doCodonDictionary
import doCodons
import sys

sys.path.insert(0, '../db/')
sys.path.insert(0, '../')

def doTotCodonUsage():
     def doCodons(dna_sequence):
     """ Functions to process DNA sequence Tot codon usage
     input: dna sequence
     output: count of codon"""
     d = doCodonDictionary()
     dna_sequence = db_summary(cg.dbArg7)
     codon_count = 0
     codon = doCodons(dna_sequence)
     
     for key in d:
          if key == codon:
               d[key] += 1
               codon_count += 1

     for key in d:
          d[key] = round((d[key]/codon_count), 3)

     return d
