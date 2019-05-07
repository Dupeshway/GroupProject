#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Processed with Restriciton Enzyme
File:doRestrictionEnzymes.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process DNA sequence incorporating restriction enzyme
--------------------------------------------------------------------------
Import libraries:
import doSelectCDS
import doEcoRI
import doBamHI
import doBsuMI
import re
"""
import doSelectCDS
import doEcoRI
import doBamHI
import doBsuMI

"""Process Restriction Enzyme"""
def doRestrictionEnzymes(input_type, input_value):
     """ Process DNA function with restriction enzyme
     Input: input type and value in config 
     Output:DNA seq after restriction enzyme """
     x = doSelectCDS(input_type, input_value)
     y = doEcoRI(x)
     z = doBamHI(y)
     dna_sequence = doBsuMI(z)
     
     return dna_sequence
