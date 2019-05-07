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
from SQL_python_functions import db_summary
from configFile import *
"""
from SQL_python_functions import db_summary
from configFile import *

"""Summary Functions Module"""
class doTotSummaryFunctions:

     """ Summary of Accssion Number"""
     def getTotAccessionNumber():
          accession_number = db_summary(dbArg1)
          return accession_number
      """ Summary of Chromosome Location"""
     def getTotChrLocation():
          chr_location = db_summary(dbArg2)
          return chr_location
     """ Summary of Gene Id """
     def getTotGeneID():
          gene_id = db_summary(dbArg3)
          return gene_id
     """ Summary of Product Name"""
     def getTotProductName():
          product_name = db_summary(dbArg4)
          return product_name
     """ Summary of Amino Acid Sequence"""
     def getTotAminoAcidSequence():
          amino_acid_sequence = db_summary(dbArg5)
          return amino_acid_sequence
     """ Summary of Location of CDS"""
     def getTotLocationCDS():
          cds_location = db_summary(dbArg6)
          return cds_location
     """ Summary of Location of DNA"""
     def getTotDNA():
          dna_sequence = db_summary(dbArg7)
          return dna_sequence
