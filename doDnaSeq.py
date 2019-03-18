#!/usr/bin/env python3

import re

def doDnaSeq (a) :
     '''Tests if DNA sequence is correct and capitalised
     Input: string
     Output: string
     >>> a = 'actcatcgtatagcta' #legal lower case sequence
     >>> doDnaSeq(a)
     'ACTCATCGTATAGCTA'
     >>> a = 'ATCGATCGATCGATCG' #legal upper case sequence
     >>> doDnaSeq(a)
     'ATCGATCGATCGATCG'
     >>> a = 'vbisubvsuvbosbvd' #not legal lower case sequence
     >>> doDnaSeq(a)
     'not legal DNA sequence'
     >>> a = 'NVCOIBNIOFGBINOI' #not legal upper case sequence
     >>> doDnaSeq(a)
     'not legal DNA sequence'
     >>> a = 'biybi147814' #letters/number not legal
     >>> doDnaSeq(a)
     'not legal DNA sequence'
     '''
     
     p = re.compile(r'.[^ATCGatcg]')
     seq = p.search(a)

     if seq:
          return('not legal DNA sequence')
     else:
          return(a.upper())
     

if __name__ == '__main__':
     import doctest
     doctest.testmod()
