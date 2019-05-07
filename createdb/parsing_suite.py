#!/usr/bin/env python3

#Yobi Livingstone


#PARSING SUITE
'''Parsing data'''

import re
import sys
from config import config as cg
from file_management import file_management as fm
from parse_genfile import parse_data as pd 
from cleaning_data import clean_data as cl
from SQL_format import sql_format as sf

#sys.path.insert(0, '../cgi-biocomp2/')

"""Run entire script to fully parse genbank file(r_file)"""

"""Parse ACCESSION """
fm.wipe_file(cg.sql_acc_file)
fm.write_file(pd.parse_acc_no(cg.r_file), cg.sql_acc_file)
"""WRITES TO: gene_file = 'sql_acc_no.sql'"""

"""Parse GENE_ID """
fm.wipe_file(cg.gene_file)
fm.write_file(sf.parse_gene_id(cg.r_file), cg.gene_file)
"""WRITES TO: gene_file = 'sql_gene_id.sql'"""

"""Parse CHROM_LOC """
fm.wipe_file(cg.chrom_file)
fm.write_file(sf.parse_chrom_loc(cg.r_file), cg.chrom_file)
"""WRITES TO: chrom_file = 'sql_chrom_loc.sql'"""

"""Parse PRODUCT_NAME """
fm.wipe_file(cg.prod_file)
fm.write_file(pd.parse_product_name(cg.r_file), cg.prod_file)
"""WRITES TO: prod_file= 'sql_product_name.sql'"""

"""Parse TRANSLATION (RAW DATA) """
fm.wipe_file(cg.trans_file)
fm.write_file(pd.parse_prot_trans(cg.r_file), cg.trans_file)
"""WRITES TO: trans_file = 'parsed_translation.txt'"""
 
"""Parse TRANSLATION for SQL """
fm.wipe_file(cg.sql_trans_file)
fm.write_file(sf.sql_parse_prot_trans(cg.trans_file), cg.sql_trans_file)
"""WRITES TO: sql_trans_file= 'sql_translation.sql'"""
 
"""Parse CDS_REGIONS (RAW DATA)"""
fm.wipe_file(cg.cds_file)
fm.write_file(pd.parse_cds(cg.r_file), cg.cds_file)
"""WRITES TO: cds_file = 'parsed_cds_regions.txt'"""
 
"""Parse CDS_REGIONS for SQL """
fm.wipe_file(cg.sql_cds_file)
fm.write_file(sf.sql_parse_cds(cg.cds_file), cg.sql_cds_file)
"""WRITES TO: sql_cds_file = 'sql_cds_regions.sql'"""


"""Parse DNA_SEQUENCE (RAW DATA)"""
"""***WARNING: THIS TAKES UPWARDS OF 3HRs to PARSE (CPU: i5 quad-core)***"""
fm.wipe_file(cg.dna_file)
print('Please be prepared to wait')
fm.write_file(pd.parse_dna_seq(cg.r_file), cg.dna_file)
"""WRITES TO: dna_file = 'parsed_dna_seq.txt'"""


"""Parse DNA_SEQUENCE for SQL"""
fm.wipe_file(cg.sql_dna_file)
fm.write_file(sf.sql_parse_dna_seq(cg.dna_file),cg.sql_dna_file)
"""WRITES TO: sql_dna_file = 'sql_dna_seq.sql'"""

