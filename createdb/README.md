README: Database Layer documentation

Author: Yobi Livingstone.
---------------------------------------------------------------------------------------------------------------

Contents: 

1. Parsing your data
2. Creating and populating your database 
3. Python-wrapped SQL queries
4. Database layer APIs
 
----------------------------------------------------------------------------------------------------------------
 
1) Parsing your data

Parse your data from genbank file, files found in createdb: ../GroupProject/tree/master/createdb:

i) All functions are called and run in the file parsing_suite.py. Run the entire script to fully parse your data.

ii) All files to be opened for reading and writing are specified in config.py
 
NOTE: Functions within the following classes were called to parse the data:
Cleaning_data from cleaning_data.py as cl
Config from config_db.py as cg
File_management from file_management.py as fm
Parse_data from parse_genfile.py as pd
Sql_format from SQL_format.py as sf
 
----------------------------------------------------------------------------------------------------------------
 
2) Creating and populating your database:

Open MYSQL and run the following SQL files found in createdb: ../GroupProject/tree/master/createdb:

i) CHROM8.sql (This will build your table within the database)

Next populate your table by running the following files in MYSQL:
i) sql_acc_no.sql (ACCESSION number)

ii) sql_gene_id.sql (GENE_ID, indexed by Accession numbers, some records dont have a Gene_id)

iii) sql_chrom_loc.sql (CHROM_LOC, Chromosome location, indexed by Accession number)

iv) sql_product_name.sql (PRODUCT_NAME, Protein product name, indexed by Accession number)

v) sql_translation.sql (TRANSLATION, amino acid sequence, indexed by ACCESSION)

vi) sql_cds_regions.sql (CDS_REGIONS, indexed by ACCESSION)

vii) sql_dna_seq.sql (DNA_SEQUENCE, indexed by ACCESSION)


-------------------------------------------------------------------------------------------------------------

3) Python-wrapped SQL queries:
Run SQL_python_functions.py found in cgi-biocomp2/db: ../GroupProject/cgi-biocomp2/db/SQL_python_functions.py

--------------------------------------------------------------------------------------------------------------

4) Database layer APIs:

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


--------------------------------------------------------------------------------------------------------------

Class: parse_data

        def parse_cds(datafile):
            '''This function captures the CDS region in a genbank file
            input: text file in genbank format
            output: return captured CDS region numbers, indexed by Accession
            ''' 
        
        def parse_prot_trans(datafile):
            '''This function captures the full dna sequence #KEEP WORKING ON THIS
            input: text file in genbank format
            output: return captured protein translation, indexed by Accession

        def parse_product_name(datafile):
            '''Captures the protein product name from a Genbank file
            input: chromosomal data file (genbank)
            output: protein product names, indexed by Accession, in SQL insertion format
            '''
        def simpleparse_acc_no(datafile):
            '''This function is captures lines that begin with the string: Accession
            input: text file in genbank format
            output: return captured accession numbers, each number on a new line

        def parse_acc_no(datafile):
            '''This function is to capture lines that begin
            with the string: Accession
            input: text file in genbank format
            output: return captured accession numbers ready for SQL insertion

        def parse_dna_seq(datafile):
            '''This function captures the full dna sequence
            input: text file in genbank format
            output: return captured dna seq numbers
            ''' 

--------------------------------------------------------------------------------------------------------------

 
Class: sql_format

     def sql_parse_cds(datafile):
          '''This function converts the output of parse_cds(),
          input: text file with accession number and protein translation in alternating lines
          output: returns an SQL format insertion for a database
          '''
      def sql_parse_prot_trans(datafile):
          '''This function converts the output of parse_prot_trans(),
          input: text file with accession number and protein translation in alternating lines
          output: returns an SQL format insertion for a database
          '''
      def sql_parse_dna_seq(datafile):
          '''Convert data into an SQL table insertion
          input: file with each dna seq on a seperate line
          output: read each line as separate string and write to SQL format
          '''
      def parse_gene_id(datafile):
          '''Capture one copy of feature in each record of genbank file
          input: Genbank record
          output: seperate strings for each record
          '''
      def parse_chrom_loc(datafile):
          '''Capture one copy of feature in each record of genbank file
          input: Genbank record
          output: seperate strings for each record
          '''

--------------------------------------------------------------------------------------------------------------

SQL_python_functions:

    def db_query(output_type, input_type, input_value):
            """Retrieve search query when given query parameters;
            output_type, input_type and input_value, provided by the webuser
            Input= output_type, input_type, input_value, query parameters for data retrieval
            Output= output_value within the provided parameters
            """


    def db_summary(output_type):
          '''Retreive summary of record with specified Accession no.
          Input: Accession no.
          Output: Returning entire record associated with Accession no
          '''
--------------------------------------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------------------------------------

Class config:

    '''To store all variables to be called across modules'''
    
    test_file = 'test_chrom8.txt'
    r_file = 'trimmed_chrom_8.txt'

    acc_file = 'parsed_acc_no.txt'
    sql_acc_file = 'sql_acc_no.sql'


    prod_file= 'sql_product_name.sql'

    dna_file = 'parsed_dna_seq.txt'
    acc_dna_file = 'parsed acc_dna_seq.txt'
    sql_dna_file= 'sql_dna_seq.sql'

    cds_file = 'parsed_cds_regions.txt'
    sql_cds_file = 'sql_cds_regions.sql'

    trans_file = 'parsed_translation.txt'
    sql_trans_file= 'sql_translation.sql'

    gene_file = 'sql_gene_id.sql'

    chrom_file = 'sql_chrom_loc.sql'
