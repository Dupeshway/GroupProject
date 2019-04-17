# GroupProject
YMCJ Biocomp2 Group project


API's (work in progress) 18/04/19

aa_seq - Amino Acid sequence
acc_no - Accession Number
dna_seq - our DNA sequence
clean_data - iterable that has been cleaned (usually a string)
loc_cod - local codon usage
raw_data - any kind of iterable, data for cleaning (usually a string)
tot_cod - total codon usage

test_file - small piece of r_file for testing functions
r_file - file to be opened and read
gene_file - write to sql file to store acc and dna seqs
cds_file - write to sql file to store acc, cds regions, cds sequences and amino acid sequence



Class: cleaning_data:

def clean_wspace(dna_seq):
    '''Remove whitespace and line separators in all forms
    input: raw DNA sequence
    output: raw DNA sequence without whitespace or line separation'''


def clean_nos(dna_seq):
    '''Remove all numbers from FASTA format DNA sequence
    input: raw DNA sequence in FASTA
    output: raw DNA sequence without FASTA numbers'''

def join_strings(raw_data):
    '''Join strings
    input: raw_data can be multiple strings or lists
    output: raw_data turned into a single string: clean_data'''




Class: parse_data

def parse_acc_dna(r_file):
        '''This function captures Accession numbers and whole DNA sequences
        from a variable database
        input: read file, containing sequences
        output: return captured DNA sequences
        '''


def parse_acc_no():*legacy*
    '''This function is to capture lines that begin with the string: Accession
    input: strings of each line in text file
    output: return captured accession numbers
    '''

def parse_dna_seq():*legacy*
'''This function captures whole DNA sequences from a variable database, use Biopython to understand
input: database
output: return captured DNA sequences
'''


def query():
    '''Places SQL queries in a python wrapper to be sent to the business layer
    Input: SQL query
    Output: Returns a single result of an SQL query
    '''




Class: file_management

def open_file(file):
'''Simple function to open a file for parsing
Input: text file of chromosome
Output: string of each line in text file for parsing
'''

def wipe_file(file):
'''Wipe a file
Input: w_file to clear
output: empty w_file
'''

def write_file():
    '''Writes to the file parameter
    input: takes input(database) as file to write to,
    output: database written into file'''




Class: config
'''To store all the variables necessary'''
 
   test_file = 'test_chrom8.txt'
    r_file = 'chrom_CDS_8.txt'
    acc_file = 'acc_no.txt'
    cds_file = 'CDS_parse.sql'
    gene_file = 'gene_parse.sql'



