#!/usr/bin/env python3
from SQL_python_functions import *
import doCodons
from configFile import *

def doCodonDictionary():
     d = {}
     dna_sequence = db_summary(dbArg7)
     codon = doCodons(dna_sequence)
     d[codon] = 0

     return d
