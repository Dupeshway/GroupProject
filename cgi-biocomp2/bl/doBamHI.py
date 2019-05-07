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
import re
import sys
from config import config as cg
"""

import re
import sys
from config import config as cg

sys.path.insert(0, '../')

"""Processing with BamHI"""
def doBamHI(seq):
     """ Process Sequence with restriction enzyme BamHI
     Input: Raw DNA Sequence 
     Output:DNA process with BamHI """
     f = re.compile(r'' + cg.bamHI_forward + '')
     r = re.compile(r'' + cg.bamHI_reverse + '')
     seq = f.sub(cg.bamHI_forward[0] + cg.bamHI_char + \
                 cg.bamHI_forward[1:len(cg.bamHI_forward)], seq)
     seq = r.sub(cg.bamHI_reverse[0] + cg.bamHI_char + \
                 cg.bamHI_reverse[1:len(cg.bamHI_reverse)], seq)
     
     return seq
