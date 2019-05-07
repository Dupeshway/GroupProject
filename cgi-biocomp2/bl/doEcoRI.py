#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Restriction Enzyme with EcoRI
File:doEcoRI.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process DNA sequence with restriciton enzyme ecoRI
--------------------------------------------------------------------------
from config import config as cg
import re
import sys
"""

from config import config as cg
import re
import sys

sys.path.insert(0, '../')

"""Processing with EcoRI"""
def doEcoRI(seq):
     """ Process Sequence with restriction enzyme EcoRi
     Input: Raw DNA Sequence 
     Output:DNA process with EcoRi"""
     f = re.compile(r'' + cg.ecoRI_forward + '')
     r = re.compile(r'' + cg.ecoRI_reverse + '')
     seq = f.sub(cg.ecoRI_forward[0] + cg.ecoRI_char + \
                 cg.ecoRI_forward[1:len(cg.ecoRI_forward)], seq)
     seq = r.sub(cg.ecoRI_reverse[0] + cg.ecoRI_char + \
                 cg.ecoRI_reverse[1:len(cg.ecoRI_reverse)], seq)
     
     return seq
