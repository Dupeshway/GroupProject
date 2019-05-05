#!/usr/bin/env python3
#from database_layer import db_query
import getStartCDS
import getEndCDS
import getAminoAcidSequence
import getDNA

def doAminoAcidAndCDS(input_type, input_value):
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
          
     
     
     
