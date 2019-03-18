#!/usr/bin/env python3
import re

def doCleanSeq(a):
     '''Remove invalid characters from DNA sequence
     Input : string
     Returns : string
     '''
     
     with open (a) as f:
          file = f.read()

          file = re.sub('\d+', '', file)
          file = re.sub('\s+', '', file)
          return(file)

if __name__ == '__main__':
     import doctest
     doctest.testmod()  
