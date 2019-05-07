#!/usr/bin/env python3
"""
Program:Dictionary for Condon
File:doCodonDictionary.py
Version:1.0
Date:May-7-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Dictionary for Codon of the Sequence  
--------------------------------------------------------------------------
import sys
from SQL_python_functions import *
import doCodons
from config import config as cg
"""

import sys
from SQL_python_functions import *
import doCodons
from config import config as cg

sys.path.insert(0, '../')
sys.path.insert(0, '../db/')

#""" Condon Dictionary"""
def doCodonDictionary():
     """ Functions for a dicitonary for DNA sequence for getting codon
     input: DNA sequence
     output: Codon"""
     d = {}
     dna_sequence = db_summary(cg.dbArg7)
     codon = doCodons(dna_sequence)
     d[codon] = 0

     return d
