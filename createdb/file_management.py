!/usr/bin/env python3

"""
Program:File Management 
File:file_management.py
Version:1.0
Date:May-4-2019
Author: Yobi Livingstone, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Mangaing filrd in the Database layer
--------------------------------------------------------------------------
Usage: Parsing through files in the database
--------------------------------------------------------------------------
Import libraries:
"""

""" File Management Module"""

class file_management:

    from config import config as cg

    """Parsing"""
    def open_file(r_file):
        '''Input: text file of chromosome
        Output: string of each line from input file returned for parsing
        '''

        with open(r_file,'r') as f:
            raw_data = f.read().splitlines()
        return raw_data

    """ Empty File"""
    def wipe_file(w_file):
        '''Wipe a file
        input:w_file to clear
        output: empty w_file
        '''
        
        f = open(w_file, 'a+')
        f.truncate(0) 

    """Write file parameter"""
    def write_file(datafile, w_file):
        '''Writes to the file parameter
        input 1: opens read file, defined in config, MUST BE SINGLE STRING
        input 2: writes to w_file, defined in config
        output: database written into file'''

        f = open(w_file,'a+')
        f.write(datafile)
        print('Data written to:', w_file)

    """ Write List to File Parameter"""
    def write_list(datafile, w_file):
        '''Writes to the file parameter
        input 1: opens read file, defined in config, MUST BE SINGLE STRING
        input 2: writes to w_file, defined in config
        output: database written into file'''

        f = open(w_file,'a+')
        for i in datafile:
            f.write(i)
        print('Data written to:', w_file)
