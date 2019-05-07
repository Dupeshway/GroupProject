
GroupProject
YMCJ Biocomp2 Group project



Get functions to obtain information from the database:

def getTotAccessionNumber():
          Full summary of Accession Number
def getTotChrLocation():
          Full summary of chromosome location
def getTotGeneID():
          Full summary of Gene ID
def getTotProductName():
           Full Summary of Protein Product Name
def getTotAminoAcidSequence():
           Full Summary of Amino Acid Sequence
def getTotLocationCDS():
           Full Summary of Location of CDS
def getTotDNA():
           Full Summary of DNA

def getAccessionNumber(input_type, input_value):

      Function to obtain accession number from the database

     input: database query with Arg4, type and value from the config file

     output: accession number from database 

def getAminoAcidSequence(input_type, input_value):

      Function to obtain Amino Acid Sequence  from the database

     input: database query Arg5, type, and value from the config file

     output:Amino Acid Sequence from database


def getDNA(input_type, input_value):

      Function to obtain DNA Sequence  from the database

     input: database query type and value from the config file

     output: dna_sequence from database

def getGeneID(input_type, input_value):

      Function to obtain protein GeneID  from the database

     input: database query Arg3, type, and value from the config file

     output:Gene ID from database
def getLocationCDS(input_type, input_value):

     Function to obtain CDS Location from the database

     input: database query with Arg4, type and value from the config file

     output: CDS Location from database 

def getProductName(input_type, input_value):

      Function to obtain protein product name from the database

     input: database query type and value from the config file

     output:protein product name from database 


Do function processing information gather from the database:

def doAminoAcidAndCDS(input_type, input_value):

Processing amino acid and CDS 

input: type and value from config file for dna seq, amino acid seq, coordinate start and coordinate end

output: joined cds and amino acid spadef doBamHI(seq):
Process DNA Sequence with restriction enzyme BamHI
     Input: Raw DNA Sequence 
     Output:DNA process with BamHI 

def doBsuMI(seq):
Process Sequence with restriction enzyme BsuMI
     Input: Raw DNA Sequence 
     Output:DNA process with BamHI

def doCodonDictionary():
      Functions for a dicitonary for DNA sequence for getting codon
     input: DNA sequence
     output: Codon

def doCodons(dna_sequence):

      Functions to process DNA sequence codon

     input: dna sequence

     output: Codon for DNA seq

def doEcoRI(seq):
      Process Sequence with restriction enzyme EcoRi
     Input: Raw DNA Sequence 
     Output:DNA process with EcoRi

def getEndCDS(input_value, input_value):

Process Coordine ends from the CDS location 

     Input: input type and value in config file

     Output: coordinate end of CDS location 

def doLocalCodonUsage(input_type, input_value):
      Process Coordinate ends from the Local codon usage
     Input: input type and value in config file
     Output: count for codons

def doRestrictionEnzymes(input_type, input_value):
      Process DNA function with restriction enzyme
     Input: input type and value in config 
     Output:DNA seq after restriction enzyme

def doSelectCDS(input_type,input_value):

 Process select CDS from the getLocationCDS

     Input: input type and value in config 
     Output: selected DNA Coordinate
def getStartCDS(input_value, input_value):

       Process CDS from the getLocationCDS

     Input: input type and vaule in cofig 

     Output:CDS start Coordinate 

def doTotCodonUsage():
     def doCodons(dna_sequence):
      Functions to process DNA sequence Tot codon usage
     input: dna sequence
     output: count of codon
