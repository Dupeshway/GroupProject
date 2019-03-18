#!/usr/bin/env python3

def doCDS(a, b, c):
     '''Splice CDS sequence from full DNA sequence
     Input : string, int
     Returns : string
     '''

     seq = a[(b-1):(c)]
     return(seq)

if __name__ == '__main__':
     import doctest
     doctest.testmod()    
     
