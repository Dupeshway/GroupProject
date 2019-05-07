#!/usr/bin/env python3

#Yobi Livingstone


#WORKSHOP SUITE AND ARCHIVE
'''DO NOT CALL THESE ARCHIVED FUNCTIONS AS THEY MAY INTERFERE WITH PARSED FILES'''

import re
import sys
from config import config as cg
from file_management import file_management as fm
from cleaning_data import clean_data as cl
from SQL_format import sql_format as sf

sys.path.insert(0, '../cgi-biocomp2/')

class workshop:

"""
    def sql_parse_cds(datafile):
        '''This function converts the output of parse_cds(),
        input: text file with accession number and protein trnaslation in alternating lines
        output: returns an SQL format insertion for a database
        '''
        count=0
        raw_data=[]
        clean_data=''
        acc_data=[]
        acc_count=0
        cds_count=1

        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:

                if acc_count==0:
                    clean_data+= "INSERT into CHROM8(ACCESSION, CDS_REGIONS) values ("+cl.clean_lines("'"+line+"',")
                    acc_count+=1
                    cds_count=0

                elif cds_count==0:
                    clean_data+= cl.clean_lines("'"+line+"')ON DUPLICATE KEY UPDATE CDS_REGIONS = '"+line+"';")+"\n"
                    cds_count+=1
                    acc_count=0
            
        return (clean_data)

fm.wipe_file(cg.sql_cds_file)
fm.write_file(workshop.sql_parse_cds(cg.cds_file), cg.sql_cds_file)



        def parse_cds(datafile):
            '''This function captures the CDS region in a genbank file
            input: strings of each line in text file
            ouput: return captured dna seq numbers
            '''        

            pcds=re.compile(r'CDS\s+')
            pacc=re.compile(r'ACCESSION\s+\w+')
            psincds=re.compile(r'CDS\s+join\(.*?\)|CDS\s+.*?[^,]$')

            cds_data=''
            datafile=fm.open_file(datafile)

            cds_count=0
            brack_count=0
            acc_count=0

            for line in datafile:
                if acc_count==0:
                    if pacc.findall(line):
                        cds_data+= line[12:20]+"\n"
                        acc_count+=1
                        cds_count=0


                elif cds_count==0: 
                    if psincds.findall(line): #first try to find single-line cds regions
                        cds_data+= line[21:]+"\n" #to negate the " at the end of single line cds
                        cds_count+=1
                        acc_count=0

                        
                    elif pcds.findall(line): #find multi-line cds
                        cds_data+= line[21:]
                        cds_count+= 1 #wont reset accession until all lines are captured
                            
                else:
                    for i in line:
                            
                        if i !=')': #if char is not ", collect i
                            cds_data += i.replace(' ', '')
                            

                        elif i == ')' and brack_count==0:
                            cds_data += "\n" #if char is " and count=0, collect i
                            brack_count += 1
                            cds_count=0
                            acc_count = 0
                            break

                        elif i == ')' and brack_count>0:
                            cds_data += "\n" # if char is " and count over 0, collect i
                            brack_count = 0
                            acc_count = 0
                            break

            cds_data=cl.clean_cds_region(cds_data)
            return cl.hyphenise(cds_data)

fm.wipe_file(cg.cds_file)
fm.write_file(workshop.parse_cds(cg.r_file), cg.cds_file)



    def sql_parse_prot_trans(datafile):
        '''This function converts the output of parse_prot_trans(),
        input: text file with accession number and protein trnaslation in alternating lines
        output: returns an SQL format insertion for a database
        '''
        count=0
        raw_data=[]
        clean_data=''
        acc_data=[]
        acc_count=0
        trans_count=1

        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:

                if acc_count==0:
                    clean_data+= "INSERT into CHROM8(ACCESSION, TRANSLATION) values ("+cl.clean_lines("'"+line+"',")
                    acc_count+=1
                    trans_count=0

                elif trans_count==0:
                    clean_data+= cl.clean_lines("'"+line+"')ON DUPLICATE KEY UPDATE TRANSLATION = '"+line+"';")+"\n"
                    trans_count+=1
                    acc_count=0
            
        return (clean_data)

fm.wipe_file(cg.sql_trans_file)
fm.write_file(testing.sql_parse_prot_trans(cg.trans_file), cg.sql_trans_file)

   
    def parse_prot_trans(datafile):
        '''This function camptures the full dna sequence #KEEP WORKING ON THIS
        input: strings of each line in text file
        ouput: return captured dna seq numbers
        '''        

        ptrans=re.compile(r'translation="')
        pacc=re.compile(r'ACCESSION\s+\w+')
        pshtrans=re.compile(r'translation="\w+"')

        
        prod_trans=''
        datafile=fm.open_file(datafile)

        trans_count=0
        short_trans_count=0
        brack_count=0
        acc_count=0

        for line in datafile:
            if acc_count==0:
                if pacc.findall(line):
                    prod_trans+= line[12:20]+"\n"
                    acc_count+=1
                    trans_count=0


            elif trans_count==0: 
                if pshtrans.findall(line): #find single-line translations denoted by ending with [\W"]
                    prod_trans+= line[35:-1]+"\n" #to negate the " at the end of single line translations
                    trans_count+=1
                    acc_count=0
                    
                elif ptrans.findall(line): #find multi-line translations
                    prod_trans+= line[35:]
                    trans_count+= 1
                        
            else:
                for i in line:
                        
                    if i !='"': #if char is not ", collect i
                        prod_trans += i.replace(' ', '')
                        

                    elif i == '"' and brack_count==0:
                        prod_trans += "\n" #if char is " and count=0, collect i
                        brack_count += 1
                        trans_count=0
                        acc_count = 0
                        break

                    elif i == '"' and brack_count>0:
                        prod_trans += "\n" # if char is " and count over 0, collect i
                        brack_count = 0
                        acc_count = 0
                        break


        return prod_trans

fm.wipe_file(cg.trans_file)
fm.write_file(testing.parse_prot_trans(cg.r_file), cg.trans_file)





    def parse_product_name(datafile):
        '''Captures the protein product name from a Genbank file
        input: chromosomal data file (genbank)
        output: protein product names
        '''

        pprod=re.compile(r'product="') 
        p=re.compile(r'ACCESSION\s+\w+')
        pro_prod=''
        acc_no=''
        
        prod_counter=0
        acc_count=0
        
        datafile=fm.open_file(datafile)

        for i in datafile:
            if acc_count==0:
                if p.findall(i): #finds Accession
                    pro_prod+= "INSERT into CHROM8(ACCESSION, PRODUCT_NAME) values ('"+i[12:20]+"',"
                    acc_count+=1
                    prod_count=0
                

            elif prod_count==0:
                    if pprod.findall(i):
                        pro_prod+= "'"+i[31:70]+"')ON DUPLICATE KEY UPDATE PRODUCT_NAME='"+i[31:70]+"'; \n" #finds product="[A-Z] 
                        prod_count+=1
                        acc_count=0

        return cl.remove_apost(pro_prod) #removing apostraphes and whitespaces




------------------------------------------------------------------------------------
TESTING FOR CHROMA LOCATION



----------------------------------------------------------------------------
TESTING FOR DNA:


    #update CHROM8 SET DNA_SEQUENCE = 'TTTTTATT' WHERE ACCESSION='Z11901';
    def sql_parse_dna_seq(datafile):
        '''Convert data into an SQL table insertion
        input: file with each dna seq on a seperate line
        output: read each line as seperate string and write to SQL format
        '''
        count=0
        raw_data=[]
        clean_data=''
        acc_data=[]
        acc_count=0
        dna_count=0

        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:
                if dna_count==0:
                    clean_data+="UPDATE CHROM8 SET DNA_SEQUENCE = '"+line+"'"
                    dna_count+=1
                    acc_count=0

                elif acc_count==0:
                    clean_data+= cl.clean_lines("WHERE ACCESSION='"+line+"';\n")
                    acc_count+=1
                    dna_count=0
            
        return (clean_data)

 def parse_dna_seq(datafile):
        '''This function camptures the full dna sequence
        input: strings of each line in text file
        ouput: return captured dna seq numbers
        '''        

        pdna=re.compile(r'1 [agct][agct]') #minimal approach with 2*[agct] to negate false positives
        pbrack=re.compile(r'//')
        pacc=re.compile(r'ACCESSION\s+\w+')
        
        dna_seq=''
        datafile=fm.open_file(datafile)

        brackcount=0
        acc_count=0

        for i in datafile:
            if acc_count==0:
                if pacc.findall(i):
                    dna_seq+=i[12:20]+"\n"
                    acc_count+=1
                    brackcount=0

            
            if pdna.findall(i):
                dna_seq += cl.clean_wspace(i[10:75])

            if brackcount==0 and acc_count==1 :
                if pbrack.findall(i):
                    dna_seq+="\n"
                    brackcount+=1
                    acc_count=0


        return cl.capitalise(dna_seq)
    

 
    def sql_parse_dna_seq(datafile):
        '''Convert data into an SQL table insertion
        input: file with each dna seq on a seperate line
        output: read each line as seperate string and write to SQL format
        '''
        count=0
        raw_data=[]
        clean_data=''
        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:
                clean_data+="insert into CHROM8(DNA_SEQUENCE) VALUES('"+line+"');\n"


    def parse_dna_seq(datafile):
        '''This function camptures the full dna sequence
        input: strings of each line in text file
        ouput: return captured dna seq numbers
        '''        

        pdna=re.compile(r'1 [agct][agct]') #minimal approach with 2*[agct] to negate false positives
        pbrack=re.compile(r'//')
        pacc=re.compile(r'ACCESSION\s+\w+')
        
        dna_seq=''
        datafile=fm.open_file(datafile)

        brackcount=0
        acc_count=0

        for i in datafile:
            if acc_count==0:
                if pacc.findall(i):
                    dna_seq+=i[12:20]+"/n"
                    acc_count+=1

            
            if pdna.findall(i):
                dna_seq += cl.clean_wspace(i[10:75])

            if brackcount==0 and acc_count==1 :
                if pbrack.findall(i):
                    brackcount+=1
                    acc_count=0


        return cl.capitalise(dna_seq)


    def parse_dna_seq(datafile):
        '''This function camptures the full dna sequence
        input: strings of each line in text file
        ouput: return captured dna seq numbers
        '''        

        pdna=re.compile(r'1 [agct][agct]') #minimal approach with 2*[agct] to negate false positives
        pbrack=re.compile(r'//')
        
        dna_seq=''
        datafile=fm.open_file(datafile)

        rec_count=0

        for i in datafile:
         
            if pdna.findall(i):
                dna_seq += cl.clean_wspace(i[10:75])
                rec_count+=1
                    

            if rec_count>0:
                if pbrack.findall(i):
                    dna_seq+="\n"
                    rec_count=0


        return dna_seq

fm.wipe_file(cg.dna_file)
fm.write_file(testing.parse_dna_seq(cg.r_file), cg.dna_file)


------------------------------------------------------------
TESTING FOR GENE ID

    def parse_gene_id(datafile):
        '''Capture one copy of feature in each record of genbank file
        input: Genbank record
        output: seperate strings for each record
        '''
        
        p=re.compile(r'ACCESSION\s+\w+')
        pgene=re.compile(r'gene="[A-Z]') 
        gene_id=''
        acc_no=''
        
        gene_counter=0
        acc_count=0
        
        datafile=fm.open_file(datafile)

        for i in datafile:
            if acc_count==0:
                if p.findall(i): #finds Accession
                    gene_id+= "insert into CHROMA8_DB(ACCESSION,GENE_ID) values ('"+i[12:20]+"',"
                    acc_count+=1
                    gene_count=0
                

            elif gene_count==0:
                    if pgene.findall(i):
                        gene_id+= "'"+i[28:33]+"'); \n" #finds gene="[A-Z] 
                        gene_count+=1
                        acc_count=0

        return cl.remove_apost(gene_id) #removing apostraphes and whitespaces




-------------------------------------------------------------------------------------------

#TESTING FOR CDS PARSE

    if feature.type == "CDS":

                        aa_seq=feature.qualifiers['translation']                        
                        fm.write_file("'"+aa_seq[0]+"')", cg.cds_file) #captures string inside the list []


    def parse_CDS(file):
        '''Function to parse the CDS numbers along with their accession numbers
        input: read file, genbank
        output: CDS description
        '''
        write_file= cg.cds_file
        fm.wipe_file(write_file) #wipe write file
        for rec in SeqIO.parse(file, "genbank"):# for every entry(rec) run though the following
            if rec.features:
                for feature in rec.features:
                    #gathering and cleaning accession
                    if feature.type=='CDS':
                        
                        acc= cl.remove_version(rec.id)
                        fm.write_file("insert into CDS values ('"+ acc + "',", write_file)
                        #Accession numbers


                        #chomosome location

                        
                        
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




-------------------------------------------------------------------------------------
#TESTING FOR ACC, GENE_ID AND DNA SEQ:


    def v2parse_gene_id(datafile):
        '''Capture one copy of feature in each record of genbank file
        input: Genbank record
        output: seperate strings for each record
        '''
        
        p=re.compile(r'//')
        pgene=re.compile(r'gene="[A-Z]') 
        gene_id=''

        gene_counter=0
        count=0
        datafile=fm.open_file(datafile)

        for i in datafile:
            if p.findall(i): #finds // 
                count=0
                

            elif count==0:
                    if pgene.findall(i):
                        gene_id+= i[28:33]+'\n' #finds gene="[A-Z] 
                        count+=1

        return cl.remove_apost(gene_id) #removing apostraphes and whitespaces           


    def v1parse_gene_id(datafile):
        '''This function captures lines the the gene_id
        input: strings of each line in text file
        ouput: 
        '''
        p=re.compile(r'gene="[A-Z]') 
        #there are between 6-8 letters/number in an acc_no

        gene_id=''
        raw_data=fm.open_file(datafile)
        for i in raw_data:
            if p.findall(i):
                gene_id += i[28:33]+'\n'

        return(cl.remove_apost(gene_id))
        return(cl.clean_wspace(gene_id))



    def parse_acc_no(datafile):
        '''This function is to capture lines that begin
        with the string: Accession
        input: strings of each line in text file
        ouput: return captured accession numbers
        '''
        p=re.compile(r'ACCESSION\s+\w+') 
        #there are between 6-8 letters/number in an acc_no

        acc_no=''

        for i in datafile:
            if p.findall(i):
                acc_no += i[:20]

        return acc_no



    def parse_dna_seq(datafile):

        p=re.compile(r'ORIGIN *')
        dna_seq=''
        
        for i in datafile:
            if p.findall(i):
                dna_seq += i
            
        return dna_seq


    def clean_cds_region(raw_data):
        dirt = ('j','o','i','n','{','}','(',')','+','[',']')
        for i in raw_data:
            if i == dirt:
                raw_data=raw_data.replace(i,'')
        print(raw_data)



print(legacy.parse_acc_no(cg.r_file))



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
