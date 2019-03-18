#!/usr/bin/env python3

import re

def doAaSeq(a):
     '''Print legal amino acid sequence capitalised
     Input : string
     Output : string
     >>> a = 'dhvglifwctypmcw' #legal lower case sequence
     >>> doAaSeq(a)
     'DHVGLIFWCTYPMCW'
     >>> a = 'DHVGLIFWCTYPMCW' #legal upper case sequence
     >>> doAaSeq(a)
     'DHVGLIFWCTYPMCW'
     >>> a = 'ilvnsoubvaosbgb' #not legal sequence
     >>> doAaSeq(a)
     'not legal amino acid sequence'
     >>> a = 'nwp498t3y2f.gàG' #not legal sequence
     >>> doAaSeq(a)
     'not legal amino acid sequence'
     '''
     
     
     p = re.compile(r'.[^DERKHNQSTYAGVLIPFMWCderkhnqstyagvlipfmwc]')
     seq = p.search(a)

     if seq:
          return('not legal amino acid sequence')
     else:
          return(a.upper())


if __name__ == '__main__':
     import doctest
     doctest.testmod()
