#!/usr/bin/env python3
#from database_layer import db_query
"""
Program:Prcessing Amino Acids and CDS
File:doAminoAcidAndCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function to process Amino Acid and CDS
--------------------------------------------------------------------------
imported Libraries:
import doStartCDS
import doEndCDS
import getAminoAcidSequence
import getDNA
"""
import doStartCDS
import doEndCDS
import getAminoAcidSequence
import getDNA

def doAminoAcidAndCDS(input_type, input_value):
     """ Processing amino acid and CDS 
     input: type and value from config file for dna seq, amino acid seq, coordinate start and coordinate end
     output: joined cds and amino acid space """
     dna_sequence = getDNA(input_type, input_value)
     coordinate_start = getStartCDS(input_type, input_value)
     coordinate_end = getEndCDS(input_type, input_value)
     amino_acid_sequence = getAminoAcidSequence(input_type, input_value)

     joint_cds = ''
     count = 0
     count_tot = -1
     for x in cds_start:
          a += dna_sequence[(int(coordinate_start[count])-1):(int(coordinate_end[count])-1)]
          count +=1
          count_tot += 1

     amino_acid_spaced = ''
     for x in amino_acid_sequence:
          amino_acid_spaced += ' ' + x + ' '

     return joint_cds, amino_acid_spaced
          
     
     
     
