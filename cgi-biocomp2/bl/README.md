
Business Layer README file
Author: Margherita Martorana

-----------------------------------------------------------------------------------------------------------------------------	

Contents:
1.	Function to retrieve all data from database for summary page
2.	Functions to retrieve single data from database
3.	Functions to manipulate data

------------------------------------------------------------------------------------------------------------------------------
1.	Function to retrieve all data from database for summary page

Note: the following functions do not take an input. Calling them will retrieve the specific type of data required from the database in a form of string. These functions are calling the database search function db_summary found in SQL_python_functions. The search function requires to define a variable (data to be retrieved). The variables is set as dbArg1/2/3/4/5/6/7, and they are stored in the config file.

doTotSummaryFunctions:

	getTotAccessionNumber():
‘’’Retrieve all of the accession numbers from database
		Input: none
		Output: string with all of the accession numbers’’’
	
	getTotChrLocation():
‘’’Retrieve all of the chromosomal locations from database
		Input: none
		Output: string with all of the chromosomal locations’’’

	getTotProductName(): 
‘’’Retrieve all of the product names from database
		Input: none
		Output: string with all of the product names’’’

getTotAminoAcidSequence(): 
‘’’Retrieve all of the amino acid sequences from      database
		Input: none
		Output: string with all of the amino acid sequences’’’

	getTotLocationCDS (): 
‘’’Retrieve all of the CDS locations from database
		Input: none
		Output: string with all of the CDS locations’’’

	getTotDNA():
‘’’Retrieve all of the DNA sequences from database
Input: none
		Output: string with all of the DNA sequences’’’

------------------------------------------------------------------------------------------------------------------------------

2.	Functions to retrieve single data from database

Note: these functions are used to retrieve information from the database about a single record. They are calling the db_query function found in SQL_python_functions, which requires 3 variables: output_type, input_type, input_variable. The output type is one of the dbArg stored in the config file.

getAccessionNumber(input_type, input_value):
		‘’’Retrieve single record accession number
		Input: strings of user input type and value 
		Output: string of accession number’’’

getAminoAcidSequence(input_type, input_value):
		‘’’Retrieve single record amino acid sequence
		Input: strings of user input type and value 
		Output: string of amino acid sequence’’’

getChrLocation(input_type, input_value):
		‘’’Retrieve single record chromosomal location
		Input: strings of user input type and value 
		Output: string of chromosomal location’’’

getDNA(input_type, input_value):
		‘’’Retrieve single record DNA sequence
		Input: strings of user input type and value 
		Output: string of DNA sequence’’’

getGeneID(input_type, input_value):
		‘’’Retrieve single record gene ID/IDs
		Input: strings of user input type and value 
		Output: string of gene ID/IDs’’’

getLocationCDS(input_type, input_value):
		‘’’Retrieve single record CDS locations
		Input: strings of user input type and value 
		Output: string of CDS locations’’’

getProductName(input_type, input_value):
		‘’’Retrieve single record product name/names
		Input: strings of user input type and value 
		Output: string of product name/names’’’

-----------------------------------------------------------------------------------------------------------------------------

3.	Functions to manipulate data

Note: these functions are used to manipulate the data retrieved from the database. The all require input_type and input_value as variables.

doBamHI(input_type, input_value):
		‘’’Add BamHI specific character found in config file where the enzyme cuts
		Input: strings of user input type and value 
		Output: string of sequence with added BamHI characters’’’

doBsuMI(input_type, input_value):
		‘’’Add BsuMI specific character found in config file where the enzyme cuts
		Input: strings of user input type and value 
		Output: string of sequence with added BsuMI characters’’’

doEcoRI(input_type, input_value):
		‘’’Add EcoRI specific character found in config file where the enzyme cuts
		Input: strings of user input type and value 
		Output: string of sequence with added EcoRI characters’’’

doRestrictionEnzymes(input_type, input_value):
		‘’’Merging all previous restriction enzymes characters
		Input: strings of user input type and value 
		Output: string of sequence with added restriction enzyme characters’’’

doStartCDS(input_type, input_value):
		‘’’Add character from config file for cds start
		Input: string of user input type and value
		Output: string of sequence with start cds character’’’

doEndCDS(input_type, input_value):
		‘’’Add character from config file for cds end
		Input: string of user input type and value
		Output: string of sequence with end cds character’’’

doSelectCDS(input_type, input_value):
		‘’’Merge cds starts and ends
		Input: string of user input type and value
		Output: string of sequence with start and end cds characters’’’

doAminoAcidAndCDS(input_type, input_value):
		‘’’Merge cds starts and ends with spaced amino acid sequence
		Input: string of user input type and value
		Output: string of dna sequence with start and end cds characters and spaced amino acid sequence’’’

doCodons(input_type, input_value):
		‘’’Find codons in dna sequence
		Input: string of user input type and value
		Output: codons’’’

doCodonDictionary(input_type, input_value):
			‘’’Build the codon dictionary
			Input: string of user input type and value
			Output: dictionary of codons’’’

doLocalCodonUsage(input_type, input_value):
			‘’’Do codon usage for a specific record
			Input: string of user input type and value
			Output: dictionary of codons with related ratio’’’

doTotCodonUsage():
			‘’’Do codon usage for all of the records
			Note: this function does not need variables
			Input: none
			Output: dictionary of codons with overall ration’’’

