#!/usr/bin/env python3
#from database_layer import db_query
from configFile import *
import re

def doBsuMI(seq):
     f = re.compile(r'' + bsuMI_forward + '')
     r = re.compile(r'' + bsuMI_reverse + '')
     seq = f.sub(bsuMI_forward[0] + bsuMI_char + \
                 bsuMI_forward[1:len(bsuMI_forward)], seq)
     seq = r.sub(bsuMI_reverse[0] + bsuMI_char + \
                 bsuMI_reverse[1:len(bsuMI_reverse)], seq)
     return seq
