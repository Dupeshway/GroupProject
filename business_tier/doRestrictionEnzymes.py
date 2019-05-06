#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Start CDS
File:doStartCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to process DNA sequence incorporating restriciton enzyme
--------------------------------------------------------------------------
Import libraries:
import getDNA
import doEcoRI
import doBamHI
import doBsuMI
import re
"""
import getDNA
import doEcoRI
import doBamHI
import doBsuMI
import re

def doRestrictionEnzymes(input_type, input_value):
     """ Process DNA function with restriction enzyme
     Input: input type and vaule in cofig 
     Output:CDS start Coordinate """
     x = getDNA(input_type, input_value)
     y = doEcoRI(x)
     z = doBamHI(y)
     dna_sequence = doBsuMI(z)
     return dna_sequence
