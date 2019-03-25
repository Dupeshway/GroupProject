#!/usr/bin/env python3

#basic python wrapper for SQL queries
'''
Program:
File:

Version:
Date:
Function: to wrap SQL queries in python language

Author: Yobi Livingstone
Address: Biological Sciences, Birkbeck ...

--------------------------------------------------------------------------
Description:


--------------------------------------------------------------------------
Usage:

--------------------------------------------------------------------------
Revision History:


--------------------------------------------------------------------------
Import libraries

--------------------------------------------------------------------------
'''

def query():
    '''placing SQL queries in a python wrapper to be sent to the business layer
    input:
    output
    '''

    import sqlite3

    
    sql = ('select field1, field2, field3, field4 '
       'from table '
       'where condition1=1 '
       'and condition2=2 ')



