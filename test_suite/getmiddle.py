#!/usr/bin/env python3

"""
Program:Test Suite middle layer
File:getmiddle.py
Version:1.0
Date:May-4-2019
Function: 
Author: Jeff Li
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description:selenium To test for middle layer
--------------------------------------------------------------------------
Usage: Testing for middle layer 
--------------------------------------------------------------------------
"""
import unittest

class test_Get_function(unittest.TestCase):

    """
    Test Get funcitons froom Database
    """
    global dna
    dna = "GCG"
    global protein_sequence
    protein_sequence = "LEU"
    global ac_number
    ac_number = "12324.3"
    global info
    info = ""
    
    def test_getProductName(self,protein_sequence):
        pass
        #Get Protein product name 
    def test_getLocationCDS(self, info):
        pass
        # CGet CDS location 
    def test_getGeneID(self, info):
        pass
        # Get Gene ID  

    def test_getChrLocation(self, ac_number):
        pass
        #Get Chromosome Location
    
    def test_getAminoAcidSequence(self, dna):
        pass
        #Get amino acid seq 
    def test_getAccessionNumber(self, ac_number):
        pass
        # Get acession number

if __name__ == '__main__':
    unittest.main()


class test_Do_function(unittest.TestCase):

    """
    Test Do funcitons froom Database
    """
    global dna
    dna = "GCG"
    global protein_sequence
    protein_sequence = "LEU"
    global ac_number
    ac_number = "12324.3"
    global info
    info = ""
    
    def test_doAminoAcidAndCDS(self, info):
        pass
        #Processing amino acid and CDS
    def test_doBsuMI(self, seq):
        pass
        #Process Sequence with restriction enzyme BsuMI
    def test_doCodonDictionary(self):
        pass
        #Functions for a dicitonary for DNA sequence for getting codon
    def test_doCodons(self,dna_sequence):
        pass
        #Functions to process DNA sequence codon
    def Test_doEcoRI(self, seq):  
        pass 
        #Process Sequence with restriction enzyme EcoRi
    def test_getEndCDS(self,info):
        pass
        #Process Coordinate ends from the CDS
    def test_doLocalCodonUsage(self,info):
        pass  
        #Process Coordinate ends from the Local codon usage
    def doRestrictionEnzymes(self,info):    
        pass
        #Process DNA function with restriction enzyme
    def doSelectCDS(self,info):
        #Process select CDS from the getLocationCDS
    def getStartCDS(self,info):   
        #Process CDS from the getLocationCDS

if __name__ == '__main__':
    unittest.main()
