#!/usr/bin/env python3

def doDictCodon(str, num):
     '''Create a dictionary of codons
     Input : string, int
     Output: dictionary
     '''
     
     d = {}
     by_num = [str[i:i+num] for i in range(0, len(str), num)]
     for x in by_num:
          d[x] = 0
     return (d)
     

if __name__ == '__main__':
     import doctest
     doctest.testmod()  
