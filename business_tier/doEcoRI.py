#!/usr/bin/env python3
#from database_layer import db_query
from configFile import *
import re

def doEcoRI(seq):
     f = re.compile(r'' + ecoRI_forward + '')
     r = re.compile(r'' + ecoRI_reverse + '')
     seq = f.sub(ecoRI_forward[0] + ecoRI_char + \
                 ecoRI_forward[1:len(ecoRI_forward)], seq)
     seq = r.sub(ecoRI_reverse[0] + ecoRI_char + \
                 ecoRI_reverse[1:len(ecoRI_reverse)], seq)
     return seq
