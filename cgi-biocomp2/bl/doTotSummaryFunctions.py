#!/usr/bin/env python3

"""
Program:Summary Functions
File:doTotSummaryFunctions.py
Version:1.0
Date:May-7-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Reuturn Summary from the database 
--------------------------------------------------------------------------
imported Libraries:
from config import config as cg
from SQL_python_functions import db_summary
import sys
"""
from config import config as cg
from SQL_python_functions import db_summary
import sys

sys.path.insert(0, '../db/')
sys.path.insert(0, '../')

#"""Summary Functions Module"""

def getTotAccessionNumber():
     """Full summary of Accession Number"""
     accession_number = db_summary(cg.dbArg1)
     return accession_number

def getTotChrLocation():
     """Full summary of chromosome location"""
     chr_location = db_summary(cg.dbArg2)
     return chr_location
  
def getTotGeneID():
     """Full summary of Gene ID"""
     gene_id = db_summary(cg.dbArg3)
     return gene_id
     
def getTotProductName():
     """ Full Summary of Protein Product Name"""
     product_name = db_summary(cg.dbArg4)
     return product_name

def getTotAminoAcidSequence():
     """ Full Summary of Amino Acid Sequence"""
     amino_acid_sequence = db_summary(cg.dbArg5)
     return amino_acid_sequence

def getTotLocationCDS():
     """ Full Summary of Location of CDS"""
     cds_location = db_summary(cg.dbArg6)
     return cds_location

def getTotDNA():
     """ Full Summary of DNA"""
     dna_sequence = db_summary(cg.dbArg7)
     return dna_sequence
