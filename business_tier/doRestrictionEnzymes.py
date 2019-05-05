#!/usr/bin/env python3
#from database_layer import db_query
import getDNA
import doEcoRI
import doBamHI
import doBsuMI
import re

def doRestrictionEnzymes(input_type, input_value):
     x = getDNA(input_type, input_value)
     y = doEcoRI(x)
     z = doBamHI(y)
     dna_sequence = doBsuMI(z)
     return dna_sequence
