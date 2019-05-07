#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Restriction Enzyme with BamHI
File:doBamHI.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process DNA sequence with restriciton enzyme BamHI
--------------------------------------------------------------------------
from configFile import *
import re
"""

from configFile import *
import re

"""Processing with BamHI"""
def doBamHI(seq):
     """ Process Sequence with restriction enzyme BamHI
     Input: Raw DNA Sequence 
     Output:DNA process with BamHI """
     f = re.compile(r'' + bamHI_forward + '')
     r = re.compile(r'' + bamHI_reverse + '')
     seq = f.sub(bamHI_forward[0] + bamHI_char + \
                 bamHI_forward[1:len(bamHI_forward)], seq)
     seq = r.sub(bamHI_reverse[0] + bamHI_char + \
                 bamHI_reverse[1:len(bamHI_reverse)], seq)
     return seq
