#!/usr/bin/env python3

#remove spaces and numbers from DNA_seq

def clean_wspace(dna_seq):
    '''Remove white space and line seperators in all forms
    input: raw DNA sequence
    output: raw DNA sequence without whitespace or line seperation'''
    
    dna_seq = dna_seq.replace('\n', '')
    dna_seq = dna_seq.replace(' ', '')
    return(dna_seq)


def clean_nos(dna_seq):
    '''Remove all numbers from FASTA format DNA sequence
    input: raw DNA sequence in FASTA
    output: raw DNA sequence without FASTA numbers'''
    
    nos = ['0','1','2','3','4','5','6','7','8','9']
    dna_seq = dna_seq.replace(nos, '')
    return(dna_seq)
