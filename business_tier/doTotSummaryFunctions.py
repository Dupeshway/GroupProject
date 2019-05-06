#!/usr/bin/env python3
from SQL_python_functions import db_summary
from configFile import *

class doTotSummaryFunctions:

     def getTotAccessionNumber():
          accession_number = db_summary(dbArg1)
          return accession_number

     def getTotChrLocation():
          chr_location = db_summary(dbArg2)
          return chr_location

     def getTotGeneID():
          gene_id = db_summary(dbArg3)
          return gene_id

     def getTotProductName():
          product_name = db_summary(dbArg4)
          return product_name

     def getTotAminoAcidSequence():
          amino_acid_sequence = db_summary(dbArg5)
          return amino_acid_sequence

     def getTotLocationCDS():
          cds_location = db_summary(dbArg6)
          return cds_location

     def getTotDNA():
          dna_sequence = db_summary(dbArg7)
          return dna_sequence
