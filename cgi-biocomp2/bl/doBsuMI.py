#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Restriction Enzyme with BsuMI
File:doBsuMI.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process DNA sequence with restriciton enzyme BsuMI
--------------------------------------------------------------------------
import re
import sys
sys.path.insert(0, '../')
from config import config as cg
"""

import re
import sys
sys.path.insert(0, '../')
from config import config as cg

#"""Processed Sequence with BsuMI"""
def doBsuMI(seq):
     """ Process Sequence with restriction enzyme BsuMI
     Input: Raw DNA Sequence 
     Output:DNA process with BsuMI"""
     f = re.compile(r'' + cg.bsuMI_forward + '')
     r = re.compile(r'' + cg.bsuMI_reverse + '')
     seq = f.sub(cg.bsuMI_forward[0] + cg.bsuMI_char + \
                 cg.bsuMI_forward[1:len(cg.bsuMI_forward)], seq)
     seq = r.sub(cg.bsuMI_reverse[0] + cg.bsuMI_char + \
                 cg.bsuMI_reverse[1:len(cg.bsuMI_reverse)], seq)
     
     return seq
