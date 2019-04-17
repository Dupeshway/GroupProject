#!/usr/bin/env python3

#Yobi Livingstone


#TEST SUITE
'''only for testing functions'''

import re
from Bio import SeqIO
from Bio import SeqRecord as sr
from config import config as cg
from file_management import file_management as fm
from parse_data import parsing as pg
from cleaning_data import clean_data as cl

pg.parse_acc_dna(cg.r_file)
"""
#TESTING FOR CDS PARSE

    def parse_CDS(file):
        '''Function to parse the CDS numbers along with their accession numbers
        input: read file, genbank
        output: CDS description
        '''
        write_file= cg.cds_file
        fm.wipe_file(write_file)
        for rec in SeqIO.parse(file, "genbank"):
            if rec.features:
                for feature in rec.features:
                    #gathering and cleaning accession
                    if feature.type=='CDS':
                        acc= cl.remove_version(rec.id)
                        fm.write_file("insert into CDS values ('"+ acc + "',", write_file)
                        #Accession numbers
                        
                        cds_region= cl.clean_cds_region(feature.location)
                        fm.write_file("'"+cds_region+"',", write_file)
                        #CDS regions
                        try:
                            cds_seq=str(feature.location.extract(rec).seq)
                            fm.write_file("'"+cds_seq+"'); \n", write_file)
                            #CDS sequence
                        except:
                            fm.write_file("'CDS ERROR; FULL DNA SEQUENCE:"+str(rec.seq) +"');\n", write_file)
                            continue

testing.parse_CDS(cg.r_file)



-------------------------------------------------------------------------------------
#TESTING FOR ACC and DNA SEQ:

    def LEGACYparse_acc_dna():
        '''Using Biopython to parse Accession numbers
        input: empty, indirectly
        output: Accession numbers
        '''
        fm.wipe_file(cg.acc_file)

        for i in SeqIO.parse(cg.r_file, "genbank"):
            acc= cl.remove_version(i.id)
            fm.write_file(acc + '\n', cg.acc_file)

parse_acc()
print(cl.remove_version(12345678.1))

clean=cl.clean_cds_region('join(<1..29,453..>607)')
print(clean)


    def parse_acc_dna(r_file):
        '''This function captures Accession numbers and whole DNA sequences
        from a variable database
        input: read file, containing sequences
        output: return captured DNA sequences
        '''
        write_file=cg.gene_file
        fm.wipe_file(write_file)
        for record in SeqIO.parse(cg.r_file, "genbank"):
            acc= cl.remove_version(record.id)
            fm.write_file("insert into GENE values ('"+ acc + "', '", write_file)
            fm.write_file(str(record.seq) +"'); \n", write_file)




----------------------------------------------------------------
TESTING FOR CAPTURING AMINO ACID SEQUENCE

                for feature in rec.features:
                    aa_seq=feature.qualifiers['translation']                        
                    fm.write_file("'"+aa_seq[0]+"')", cg.cds_file) 
#captures string inside the list []
-------------------------------------------------------------------------------------
TESTING FOR CAPTURING ACC_NO

open file > parse acc > capture only first ACC_NO 


raw_data= fm.open_file(cg.r_file)
#print(raw_data)

acc_no=pg.parse_acc_no(raw_data)
#parse raw_data into accession numbers (each returned in loop)


fm.write_file(acc_no,cg.w_file)
#write parsed data into w_file)


-------------------------------------------------------------------------------------
TESTING FOR FILE MANAGEMENT:

raw_data = fm.open_file(cg.r_file)
#opens r_file and reads into raw_data

clean_data=cl.join_strings(raw_data)
#joins all strings and reads into clean_data

fm.write_file(clean_data, cg.w_file)
#writes the clean_data into the w_file

"""
