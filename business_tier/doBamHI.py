#!/usr/bin/env python3
#from database_layer import db_query
from configFile import *
import re

def doBamHI(seq):
     f = re.compile(r'' + bamHI_forward + '')
     r = re.compile(r'' + bamHI_reverse + '')
     seq = f.sub(bamHI_forward[0] + bamHI_char + \
                 bamHI_forward[1:len(bamHI_forward)], seq)
     seq = r.sub(bamHI_reverse[0] + bamHI_char + \
                 bamHI_reverse[1:len(bamHI_reverse)], seq)
     return seq
