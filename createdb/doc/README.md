# GroupProject
YMCJ Biocomp2 Group project

----------------------------------------------------------------------------

Documentation: (creating your database)

Open mysql and run the following sql files:

1. CHROM8.sql (This will build your table)

2. Next populate your database by running the following files in mysql:

    i) acc_no.sql (ACCESSION number)
    
    ii) gene_parse.sql (GENE_ID, indexed by Accession numbers, some records dont have Gene_id)
    
    iii) product_parse.sql (PRODUCT_NAME, Protein product name, some records dont have or use multiple)
    
    iv) parse_chrom_loc.sql (CHROM_LOC, Chromosome location, indexed by Accession number)
    
    v) sql_dna_seq.sql (DNA_SEQUENCE indexed by ACCESSION)
    
    vi) sql_trans_parse.sql (TRANSLATION, Protein translation, amino acid sequence, indexed by ACCESSION)


Notes:

Resolved to combine 2 files(raw_acc_no.sql, dna_seq.sql) with alternating lines using linux terminal command: $ paste -d \\n raw_acc_no.sql dna_seq.sql > acc_dna_seq.txt

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

input_type=var#
input_value=var#
output_value=var#

def db_query(var1, var2, var3): THESE VARIABLES ARE USED IN SQL QUERY
	Sql = select var1 from chrom8 where var2 = var3
	Returning sql

Def db_summary(var1):
	Slq = Select var1 from chrom8
	Return sql



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


