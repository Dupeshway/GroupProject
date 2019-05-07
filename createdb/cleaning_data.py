#!/usr/bin/env python3

#Yobi Livingstone

"""
Program:Cleaning Data
File:cleaning_data.py
Version:1.0
Date:May-4-2019
Author: Yobi Livingstone, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Functions to clean raw data 
--------------------------------------------------------------------------
Usage: For processing data to the bussiness layer to make it consistent
and easier to handle.
--------------------------------------------------------------------------
Import libraries: re
"""

import re

""" Cleaning Module """"

class clean_data:
    '''Every function is intended to join, remove, replace iterables (strings, lists etc)
    to make the data easier to handle after capturing/parsing'''

""" Joining Raw Data"""
    
    def join_strings(raw_data):
        '''Join strings
        input: raw_data be multiple strings or lists
        output: raw_data turned into a single string: clean_data'''

        clean_data=''
        clean_data=clean_data.join(raw_data)
        return clean_data
    
""" CDS Cleaning """

    def clean_cds_region(raw_data):
        """ Cleaning CDS region
        input: raw_data clean data
        output: cleaned raw data
        """
        raw_data=str(raw_data)
        clean_data=re.sub('[join()<>+{}]','', raw_data)
        return clean_data

    def clean_cds_loc(raw_data):
        """ Cleaning cds location
        input: raw_data clean data 
        output: raw_data with i removed
        """
        dirt = ('j','o','i','n','{','}','(',')','+','[',']')
        for i in raw_data:
            if i == dirt:
                raw_data=raw_data.replace(i,'')
        print(raw_data)

        
"""PROTEIN TRANSLATION"""
        
    def remove_apost(raw_data):
         """ Cleaning
        input: raw_data clean data 
        output: raw_data space removed
        """
        clean_data = raw_data.replace('"','')
        return clean_data

""" Remove Version Nunmber in Acession_No """
    def remove_version(acc_no):
        '''Accession numbers captured have a version number after a decimal point
        at the end of the number i.e AB12345678.1 This removes the version number [.1]
        input:Accession numbers with version number attached
        output: Accession number without version number attached
        '''
        acc_no=str(acc_no)
        for i in acc_no:
            if i=='.':
                acc_no = acc_no[:-2] #captures all except the last two places
        return acc_no

""" White space removal """"
    def clean_wspace(dna_seq):
        '''Remove white space and line seperators in all forms
        input: raw DNA sequence
        output: raw DNA sequence without whitespace or line seperation'''
    
        dna_seq = dna_seq.replace('\n', '')
        dna_seq = dna_seq.replace(' ', '')
        return(dna_seq)

""" Line Removal """"
    def clean_lines(raw_data):
        '''Remove line seperators in all forms
        input: raw DNA sequence
        output: raw DNA sequence without empty lines seperation'''
    
        raw_data = raw_data.replace('\n', '')
        return(raw_data)

"""Removing Number in DNA sequence """

    def clean_nos(raw_data):
        '''Remove all numbers from FASTA format DNA sequence
        input: raw DNA sequence in FASTA
        output: raw DNA sequence without FASTA numbers'''
    
        nos = ['0','1','2','3','4','5','6','7','8','9']
        dna_seq = dna_seq.replace(nos, '')

        return(dna_seq)

""" Capitalise All"""
    
    def capitalise(raw_data):
        '''Entire string is capitalised
        input: single string in upper and lowercase forms
        output: single string all uppercase
        '''
        uppercase=''
        for i in raw_data:
            dna_seq=raw_data.upper()
        return dna_seq

 """ Ignore N's"""

    def ignore_nnn(raw_data):
        '''ignore database codon entries with N
        Input: string(DNA seq) is read from text file
        Output: clean_string without N is passed through, codons with N is ignored
        '''
        clean_string=''
    
        for i in raw_data:
            if i!='N' or 'n':
                clean_string.append(string)
            else:
                continue
    
        return clean_string



