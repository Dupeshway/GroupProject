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
