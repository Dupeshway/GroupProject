#!/usr/bin/env python3
"""
Program:Dictionary for Condon
File:doCodonDictionary.py
Version:1.0
Date:May-7-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Dictionary for Codon of the Sequenc  
--------------------------------------------------------------------------
from SQL_python_functions import *
import doCodons
from configFile import *
"""
from SQL_python_functions import *
import doCodons
from configFile import *

""" Condon Dictionary"""
def doCodonDictionary():
     """ Functions for a dicitonary for DNA sequence codon
     input: dna sequence
     output: DNA sequnce with the codon"""
     d = {}
     dna_sequence = db_summary(dbArg7)
     codon = doCodons(dna_sequence)
     d[codon] = 0

     return d
